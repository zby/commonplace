from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import sqlite3

import pytest

from commonplace.review import review_db, review_schema
from tests.commonplace.review.pair_helpers import accept_pair, insert_completed_pair


def test_ensure_db_initializes_current_schema(tmp_path: Path) -> None:
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
                accepted_review_pair_id,
                accepted_note_snapshot_id,
                accepted_gate_snapshot_id,
                accepted_note_hash,
                accepted_gate_hash
            FROM current_gate_acceptances
            WHERE note_path = 'kb/notes/fresh.md'
            """
        ).fetchone()
        user_version = conn.execute("PRAGMA user_version").fetchone()[0]
        job_columns = {row["name"]: row for row in conn.execute("PRAGMA table_info(review_jobs)").fetchall()}
        pair_columns = {row["name"] for row in conn.execute("PRAGMA table_info(review_pairs)").fetchall()}
        acceptance_columns = {
            row["name"]: row
            for row in conn.execute("PRAGMA table_info(acceptance)").fetchall()
        }
        index_names = {
            row["name"]
            for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type = 'index'"
            ).fetchall()
        }
        table_names = {
            row["name"]
            for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type = 'table'"
            ).fetchall()
        }

    assert view_row is not None
    assert view_row["accepted_review_pair_id"] == review_pair_id
    assert view_row["accepted_note_snapshot_id"] is None
    assert view_row["accepted_gate_snapshot_id"] is None
    assert view_row["accepted_note_hash"] is None
    assert view_row["accepted_gate_hash"] is None
    assert user_version == review_schema.REVIEW_SCHEMA_VERSION
    assert "created_at" in job_columns
    assert "started_at" not in job_columns
    assert job_columns["runner"]["notnull"] == 0
    assert "runner_model" in job_columns
    assert "runner_effort" in job_columns
    assert "prompt_path" not in job_columns
    assert "bundle_output_path" not in job_columns
    assert "model_partition" not in pair_columns
    assert "pair_status" not in pair_columns
    assert "result_path" not in pair_columns
    assert "acceptance_event_id" not in acceptance_columns
    assert acceptance_columns["accepted_review_pair_id"]["notnull"] == 1
    assert "idx_review_pairs_note_gate" in index_names
    assert "idx_review_pairs_note_gate_model_partition" not in index_names
    assert "idx_acceptance_note_gate_model_partition" in index_names
    assert "idx_acceptance_events_latest_by_key" not in index_names
    assert table_names == {
        "acceptance",
        "review_file_snapshots",
        "review_jobs",
        "review_pairs",
    }


def test_ensure_db_rejects_stale_review_store_shape(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db_path) as conn:
        conn.execute("CREATE TABLE review_jobs (review_job_id INTEGER PRIMARY KEY)")
        conn.commit()

    with pytest.raises(RuntimeError, match="does not match current version"):
        review_db.ensure_db(db_path)


def test_upsert_acceptance_requires_review_pair(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        invalid_pair_id = None
        with pytest.raises(ValueError, match="accepted_review_pair_id is required"):
            review_db.upsert_acceptance(
                conn,
                note_path="kb/notes/current.md",
                gate_path="kb/instructions/review-gates/prose/current.md",
                model_partition="opus-4-6",
                accepted_review_pair_id=invalid_pair_id,
                accepted_at="2026-04-10T10:02:00+02:00",
            )


def test_db_checks_remain_final_enum_backstop(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        with pytest.raises(sqlite3.IntegrityError):
            conn.execute(
                """
                INSERT INTO review_jobs (
                    model_partition,
                    created_at,
                    status,
                    packing
                ) VALUES (?, ?, ?, ?)
                """,
                ("test-model", "2026-04-10T10:03:00+02:00", "waiting", "note"),
            )
        with pytest.raises(sqlite3.IntegrityError):
            conn.execute(
                """
                INSERT INTO review_jobs (
                    model_partition,
                    created_at,
                    status,
                    packing
                ) VALUES (?, ?, ?, ?)
                """,
                ("test-model", "2026-04-10T10:03:00+02:00", "queued", "bundle"),
            )
        review_job_id = review_db.create_job(
            conn,
            model_partition="test-model",
            runner=None,
            created_at="2026-04-10T10:03:00+02:00",
            status="queued",
            packing="note",
        )
        with pytest.raises(sqlite3.IntegrityError):
            conn.execute(
                """
                INSERT INTO review_pairs (
                    review_job_id,
                    note_path,
                    gate_path,
                    pair_ordinal,
                    decision
                ) VALUES (?, ?, ?, ?, ?)
                """,
                (
                    review_job_id,
                    "kb/notes/current.md",
                    "kb/instructions/review-gates/prose/current.md",
                    0,
                    "maybe",
                ),
            )


def test_model_partition_writes_are_canonicalized(tmp_path: Path) -> None:
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
        job_model = conn.execute("SELECT model_partition FROM review_jobs").fetchone()[0]
        acceptance_model = conn.execute("SELECT model_partition FROM acceptance").fetchone()[0]

    assert job_model == "claude-opus"
    assert acceptance_model == "claude-opus"


def test_current_acceptance_view_filters_incomplete_jobs_and_null_decisions(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        current_pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/fresh.md",
            gate_id="semantic/internal-consistency",
            model_partition="opus-4-6",
            decision="pass",
            reviewed_at="2026-04-10T10:01:00+02:00",
        )
        accept_pair(
            conn,
            review_pair_id=current_pair_id,
            note_path="kb/notes/fresh.md",
            gate_id="semantic/internal-consistency",
            model_partition="opus-4-6",
            accepted_at="2026-04-10T10:02:00+02:00",
        )
        queued_job_id = review_db.create_job_with_pairs(
            conn,
            model_partition="opus-4-6",
            runner="test-runner",
            created_at="2026-04-10T10:03:00+02:00",
            status="queued",
            packing="note",
            pairs=[
                review_db.ReviewPairRequest(
                    note_path="kb/notes/queued.md",
                    gate_path="kb/instructions/review-gates/semantic/internal-consistency.md",
                    pair_ordinal=0,
                )
            ],
        )
        review_db.complete_review_pairs(
            conn,
            review_job_id=queued_job_id,
            review_pairs=[
                review_db.ReviewPairCompletion(
                    note_path="kb/notes/queued.md",
                    gate_path="kb/instructions/review-gates/semantic/internal-consistency.md",
                    decision="warn",
                    reviewed_at="2026-04-10T10:03:30+02:00",
                )
            ],
            reviewed_at="2026-04-10T10:03:30+02:00",
        )
        queued_pair_id = review_db.load_review_pairs_for_job(conn, review_job_id=queued_job_id)[0].review_pair_id
        accept_pair(
            conn,
            review_pair_id=queued_pair_id,
            note_path="kb/notes/queued.md",
            gate_id="semantic/internal-consistency",
            model_partition="opus-4-6",
            accepted_at="2026-04-10T10:04:00+02:00",
        )
        null_decision_job_id = review_db.create_job_with_pairs(
            conn,
            model_partition="opus-4-6",
            runner="test-runner",
            created_at="2026-04-10T10:05:00+02:00",
            status="completed",
            packing="note",
            pairs=[
                review_db.ReviewPairRequest(
                    note_path="kb/notes/null-decision.md",
                    gate_path="kb/instructions/review-gates/semantic/internal-consistency.md",
                    pair_ordinal=0,
                )
            ],
        )
        null_decision_pair_id = review_db.load_review_pairs_for_job(
            conn,
            review_job_id=null_decision_job_id,
        )[0].review_pair_id
        conn.execute(
            """
            INSERT INTO acceptance (
                note_path,
                gate_path,
                model_partition,
                accepted_review_pair_id,
                accepted_at
            ) VALUES (?, ?, ?, ?, ?)
            """,
            (
                "kb/notes/null-decision.md",
                "kb/instructions/review-gates/semantic/internal-consistency.md",
                "claude-opus",
                null_decision_pair_id,
                "2026-04-10T10:06:00+02:00",
            ),
        )

        view_row = conn.execute(
            """
            SELECT accepted_review_pair_id
            FROM current_gate_acceptances
            WHERE note_path = 'kb/notes/fresh.md'
            """
        ).fetchone()
        hidden_rows = conn.execute(
            """
            SELECT note_path
            FROM current_gate_acceptances
            WHERE note_path IN ('kb/notes/queued.md', 'kb/notes/null-decision.md')
            """
        ).fetchall()

    assert view_row["accepted_review_pair_id"] == current_pair_id
    assert hidden_rows == []


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


def test_load_review_job_exposes_created_at(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        review_job_id = review_db.create_job_with_pairs(
            conn,
            model_partition="opus-4-6",
            runner="live-agent",
            created_at="2026-04-10T10:03:00+02:00",
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
    assert review_job.status == "queued"


def test_create_job_validates_runner_model_partition(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        with pytest.raises(ValueError, match="does not match model_partition"):
            review_db.create_job(
                conn,
                model_partition="unknown-model-high",
                runner="live-agent",
                runner_model="unknown-model",
                created_at="2026-04-10T10:03:00+02:00",
                status="queued",
                packing="note",
            )

        review_job_id = review_db.create_job(
            conn,
            model_partition="unknown-model-high",
            runner="live-agent",
            runner_model="unknown-model",
            runner_effort="HIGH",
            created_at="2026-04-10T10:03:00+02:00",
            status="queued",
            packing="note",
        )
        row = conn.execute(
            "SELECT runner_model, runner_effort FROM review_jobs WHERE review_job_id = ?",
            (review_job_id,),
        ).fetchone()

    assert row["runner_model"] == "unknown-model"
    assert row["runner_effort"] == "high"


def test_attach_execution_data_validates_runner_model_partition(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        review_job_id = review_db.create_job(
            conn,
            model_partition="unknown-model-high",
            runner=None,
            created_at="2026-04-10T10:03:00+02:00",
            status="queued",
            packing="note",
        )

        with pytest.raises(ValueError, match="does not match model_partition"):
            review_db.attach_execution_data(
                conn,
                review_job_id=review_job_id,
                runner_model="unknown-model",
            )

        review_db.attach_execution_data(
            conn,
            review_job_id=review_job_id,
            runner_model="unknown-model",
            runner_effort="HIGH",
        )
        row = conn.execute(
            "SELECT runner_model, runner_effort FROM review_jobs WHERE review_job_id = ?",
            (review_job_id,),
        ).fetchone()

    assert row["runner_model"] == "unknown-model"
    assert row["runner_effort"] == "high"


def test_prune_superseded_acceptances_deletes_unreferenced_snapshots(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    repo = tmp_path / "repo"
    repo.mkdir()
    files = {
        "kb/notes/sample.md": "old note\n",
        "kb/instructions/review-gates/prose/sample.md": "old gate\n",
    }
    for rel_path, content in files.items():
        path = repo / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        old_note = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/sample.md")
        old_gate = review_db.snapshot_file(
            conn,
            repo_root=repo,
            path="kb/instructions/review-gates/prose/sample.md",
        )
        old_pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/sample.md",
            gate_id="prose/sample",
            model_partition="opus-4-6",
            decision="pass",
            reviewed_at="2026-04-10T10:01:00+02:00",
            reviewed_note_snapshot_id=old_note.snapshot_id,
            reviewed_gate_snapshot_id=old_gate.snapshot_id,
        )
        accept_pair(
            conn,
            review_pair_id=old_pair_id,
            note_path="kb/notes/sample.md",
            gate_id="prose/sample",
            model_partition="opus-4-6",
            accepted_at="2026-04-10T10:02:00+02:00",
            accepted_note_snapshot_id=old_note.snapshot_id,
            accepted_gate_snapshot_id=old_gate.snapshot_id,
        )

        (repo / "kb/notes/sample.md").write_text("current note\n", encoding="utf-8")
        (repo / "kb/instructions/review-gates/prose/sample.md").write_text("current gate\n", encoding="utf-8")
        current_note = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/sample.md")
        current_gate = review_db.snapshot_file(
            conn,
            repo_root=repo,
            path="kb/instructions/review-gates/prose/sample.md",
        )
        current_pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/sample.md",
            gate_id="prose/sample",
            model_partition="opus-4-6",
            decision="pass",
            reviewed_at="2026-04-10T10:03:00+02:00",
            reviewed_note_snapshot_id=current_note.snapshot_id,
            reviewed_gate_snapshot_id=current_gate.snapshot_id,
        )
        old_job_id = conn.execute(
            "SELECT review_job_id FROM review_pairs WHERE review_pair_id = ?",
            (old_pair_id,),
        ).fetchone()["review_job_id"]
        superseded = accept_pair(
            conn,
            review_pair_id=current_pair_id,
            note_path="kb/notes/sample.md",
            gate_id="prose/sample",
            model_partition="opus-4-6",
            accepted_at="2026-04-10T10:04:00+02:00",
            accepted_note_snapshot_id=current_note.snapshot_id,
            accepted_gate_snapshot_id=current_gate.snapshot_id,
        )
        deleted_job_ids = review_db.prune_superseded_acceptances(conn, [superseded])
        remaining_snapshot_ids = {
            int(row["snapshot_id"])
            for row in conn.execute("SELECT snapshot_id FROM review_file_snapshots").fetchall()
        }
        old_pair = conn.execute(
            "SELECT review_pair_id FROM review_pairs WHERE review_pair_id = ?",
            (old_pair_id,),
        ).fetchone()
        current_pair = conn.execute(
            "SELECT review_pair_id FROM review_pairs WHERE review_pair_id = ?",
            (current_pair_id,),
        ).fetchone()

    assert deleted_job_ids == {old_job_id}
    assert old_pair is None
    assert current_pair is not None
    assert old_note.snapshot_id not in remaining_snapshot_ids
    assert old_gate.snapshot_id not in remaining_snapshot_ids
    assert current_note.snapshot_id in remaining_snapshot_ids
    assert current_gate.snapshot_id in remaining_snapshot_ids


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
        review_pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/sample.md",
            gate_id="prose/sample",
            model_partition="opus-4-6",
            decision="pass",
            reviewed_at="2026-04-10T10:01:00+02:00",
            reviewed_note_snapshot_id=note_snapshot.snapshot_id,
            reviewed_gate_snapshot_id=gate_snapshot.snapshot_id,
        )
        accept_pair(
            conn,
            review_pair_id=review_pair_id,
            note_path="kb/notes/sample.md",
            gate_id="prose/sample",
            model_partition="opus-4-6",
            accepted_at="2026-04-10T10:02:00+02:00",
            accepted_note_snapshot_id=note_snapshot.snapshot_id,
            accepted_gate_snapshot_id=gate_snapshot.snapshot_id,
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
