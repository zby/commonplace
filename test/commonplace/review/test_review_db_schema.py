from __future__ import annotations

from hashlib import sha256
from importlib import resources
import sqlite3
from pathlib import Path

import pytest

from commonplace.review import review_db
from test.commonplace.review.pair_helpers import accept_pair, insert_completed_pair


REPO_ROOT = Path(__file__).resolve().parents[3]


def test_ensure_db_does_not_mutate_existing_acceptance_event_schema(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    schema_text = (resources.files("commonplace.review") / "review-schema.sql").read_text(encoding="utf-8")
    old_schema = schema_text.replace("            'gate-migration',\n", "")

    with sqlite3.connect(db_path) as conn:
        conn.executescript(old_schema)
        conn.commit()

    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        row = conn.execute(
            """
            SELECT sql
            FROM sqlite_master
            WHERE type = 'table' AND name = 'acceptance_events'
            """
        ).fetchone()

    assert row is not None
    assert "'gate-migration'" not in row["sql"].lower()


def migration_names(db_path: Path) -> list[str]:
    with review_db.connect(db_path) as conn:
        rows = conn.execute(
            """
            SELECT migration_name
            FROM review_schema_migrations
            ORDER BY migration_name
            """
        ).fetchall()
    return [row["migration_name"] for row in rows]


def test_ensure_db_initializes_schema_that_can_store_current_acceptance(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"

    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        review_pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/fresh.md",
            gate_id="semantic/internal-consistency",
            model_partition="opus-4-6",
            decision="pass",
            rationale_markdown="ok",
            gate_sha="gate-sha",
            reviewed_note_sha="note-sha",
            reviewed_note_commit="note-commit",
            reviewed_at="2026-04-10T10:01:00+02:00",
        )
        accept_pair(
            conn,
            review_pair_id=review_pair_id,
            note_path="kb/notes/fresh.md",
            gate_id="semantic/internal-consistency",
            model_partition="opus-4-6",
            accepted_note_sha="note-sha",
            accepted_note_commit="note-commit",
            accepted_gate_sha="gate-sha",
            accepted_at="2026-04-10T10:02:00+02:00",
            acceptance_kind="full-review",
        )
        view_row = conn.execute(
            """
            SELECT
                accepted_note_sha,
                accepted_gate_sha,
                accepted_note_snapshot_id,
                accepted_gate_snapshot_id,
                accepted_note_hash,
                accepted_gate_hash
            FROM current_gate_acceptances
            WHERE note_path = 'kb/notes/fresh.md'
            """
        ).fetchone()

    assert view_row is not None
    assert view_row["accepted_note_sha"] == "note-sha"
    assert view_row["accepted_gate_sha"] == "gate-sha"
    assert view_row["accepted_note_snapshot_id"] is None
    assert view_row["accepted_gate_snapshot_id"] is None
    assert view_row["accepted_note_hash"] is None
    assert view_row["accepted_gate_hash"] is None
    assert set(migration_names(db_path)) == {
        review_db.BASELINE_SCHEMA_MIGRATION,
        "review-file-snapshots-v1",
        "review-model-partition-v1",
        "review-gate-path-v1",
    }


def test_ensure_db_migrates_existing_acceptances_without_losing_current_view(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    schema_text = (resources.files("commonplace.review") / "review-schema.sql").read_text(encoding="utf-8")

    with sqlite3.connect(db_path) as conn:
        conn.executescript(schema_text)
        conn.commit()

    with review_db.connect(db_path) as conn:
        review_pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/legacy.md",
            gate_id="semantic/internal-consistency",
            model_partition="opus-4-6",
            decision="pass",
            rationale_markdown="ok",
            gate_sha="legacy-gate-sha",
            reviewed_note_sha="legacy-note-sha",
            reviewed_note_commit="legacy-note-commit",
            reviewed_at="2026-04-10T10:01:00+02:00",
        )
        accept_pair(
            conn,
            review_pair_id=review_pair_id,
            note_path="kb/notes/legacy.md",
            gate_id="semantic/internal-consistency",
            model_partition="opus-4-6",
            accepted_note_sha="legacy-note-sha",
            accepted_note_commit="legacy-note-commit",
            accepted_gate_sha="legacy-gate-sha",
            accepted_at="2026-04-10T10:02:00+02:00",
            acceptance_kind="full-review",
        )
        conn.commit()

    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        acceptances = review_db.load_current_acceptances(conn)
        view_row = conn.execute(
            """
            SELECT
                accepted_note_sha,
                accepted_note_commit,
                accepted_gate_sha,
                accepted_note_snapshot_id,
                accepted_gate_snapshot_id,
                accepted_note_hash,
                accepted_gate_hash
            FROM current_gate_acceptances
            WHERE note_path = 'kb/notes/legacy.md'
            """
        ).fetchone()
        stale_row = conn.execute(
            """
            SELECT
                accepted_note_sha,
                accepted_gate_sha,
                accepted_note_hash,
                accepted_gate_hash
            FROM stale_gate_pairs
            WHERE note_path = 'kb/notes/legacy.md'
            """
        ).fetchone()

    acceptance = acceptances[
        (
            "kb/notes/legacy.md",
            "kb/instructions/review-gates/semantic/internal-consistency.md",
            "opus-4-6",
        )
    ]
    assert acceptance.accepted_note_sha == "legacy-note-sha"
    assert acceptance.accepted_gate_sha == "legacy-gate-sha"
    assert view_row["accepted_note_commit"] == "legacy-note-commit"
    assert view_row["accepted_note_snapshot_id"] is None
    assert view_row["accepted_gate_snapshot_id"] is None
    assert view_row["accepted_note_hash"] is None
    assert view_row["accepted_gate_hash"] is None
    assert stale_row["accepted_note_sha"] == "legacy-note-sha"
    assert stale_row["accepted_gate_sha"] == "legacy-gate-sha"
    assert stale_row["accepted_note_hash"] is None
    assert stale_row["accepted_gate_hash"] is None


def test_ensure_db_renames_legacy_model_id_columns_to_model_partition(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    schema_text = (resources.files("commonplace.review") / "review-schema.sql").read_text(encoding="utf-8")
    legacy_schema = schema_text.replace("model_partition", "model_id").replace("gate_path", "gate_id")
    legacy_schema = legacy_schema.replace("idx_review_runs_model_id_started", "idx_review_runs_model_started")
    legacy_schema = legacy_schema.replace("idx_review_pairs_note_gate_model_id", "idx_review_pairs_note_gate_model")
    legacy_schema = legacy_schema.replace(
        "idx_acceptance_events_note_gate_model_id",
        "idx_acceptance_events_note_gate_model",
    )

    with sqlite3.connect(db_path) as conn:
        conn.executescript(legacy_schema)
        conn.execute(
            """
            INSERT INTO review_runs (
                review_run_id,
                model_id,
                runner,
                started_at,
                status,
                packing
            ) VALUES (1, 'opus-4-6', 'test-runner', '2026-04-10T10:00:00+02:00', 'completed', 'note')
            """
        )
        conn.execute(
            """
            INSERT INTO review_pairs (
                review_pair_id,
                review_run_id,
                note_path,
                gate_id,
                model_id,
                pair_ordinal,
                pair_status,
                decision,
                gate_sha,
                reviewed_note_sha,
                reviewed_at,
                review_kind
            ) VALUES (
                1,
                1,
                'kb/notes/legacy-model.md',
                'semantic/internal-consistency',
                'opus-4-6',
                0,
                'completed',
                'pass',
                'gate-sha',
                'note-sha',
                '2026-04-10T10:01:00+02:00',
                'full-review'
            )
            """
        )
        conn.execute(
            """
            INSERT INTO acceptance_events (
                acceptance_event_id,
                note_path,
                gate_id,
                model_id,
                accepted_review_pair_id,
                accepted_note_sha,
                accepted_gate_sha,
                accepted_at,
                acceptance_kind
            ) VALUES (
                1,
                'kb/notes/legacy-model.md',
                'semantic/internal-consistency',
                'opus-4-6',
                1,
                'note-sha',
                'gate-sha',
                '2026-04-10T10:02:00+02:00',
                'full-review'
            )
            """
        )
        conn.commit()

    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        table_columns = {
            table_name: {
                row["name"]
                for row in conn.execute(f"PRAGMA table_info({table_name})").fetchall()
            }
            for table_name in ("review_runs", "review_pairs", "acceptance_events")
        }
        run_row = conn.execute("SELECT model_partition FROM review_runs").fetchone()
        view_row = conn.execute(
            """
            SELECT gate_path, model_partition, accepted_note_sha, accepted_gate_sha
            FROM current_gate_acceptances
            WHERE note_path = 'kb/notes/legacy-model.md'
            """
        ).fetchone()

    for columns in table_columns.values():
        assert "model_partition" in columns
        assert "model_id" not in columns
    for columns in (table_columns["review_pairs"], table_columns["acceptance_events"]):
        assert "gate_path" in columns
        assert "gate_id" not in columns
    assert run_row["model_partition"] == "opus-4-6"
    assert view_row["gate_path"] == "kb/instructions/review-gates/semantic/internal-consistency.md"
    assert view_row["model_partition"] == "opus-4-6"
    assert view_row["accepted_note_sha"] == "note-sha"
    assert view_row["accepted_gate_sha"] == "gate-sha"


def test_ensure_db_applies_pending_schema_migrations_once(tmp_path: Path, monkeypatch) -> None:
    db_path = tmp_path / "review-store.sqlite"

    def apply_probe_migration(conn: sqlite3.Connection, repo_root: Path) -> None:
        del repo_root
        conn.execute("CREATE TABLE migration_probe (value TEXT NOT NULL)")
        conn.execute("INSERT INTO migration_probe (value) VALUES ('applied')")

    monkeypatch.setattr(
        review_db,
        "SCHEMA_MIGRATIONS",
        review_db.SCHEMA_MIGRATIONS + (review_db.SchemaMigration("999-test-probe", apply_probe_migration),),
    )

    review_db.ensure_db(REPO_ROOT, db_path)
    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        probe_rows = conn.execute("SELECT value FROM migration_probe").fetchall()

    assert [row["value"] for row in probe_rows] == ["applied"]
    assert set(migration_names(db_path)) == {
        review_db.BASELINE_SCHEMA_MIGRATION,
        "review-file-snapshots-v1",
        "review-model-partition-v1",
        "review-gate-path-v1",
        "999-test-probe",
    }


def test_ensure_db_normalizes_legacy_migration_table_version_column(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"

    with sqlite3.connect(db_path) as conn:
        conn.execute(
            """
            CREATE TABLE review_schema_migrations (
                version TEXT PRIMARY KEY,
                applied_at TEXT NOT NULL
            )
            """
        )
        conn.execute(
            """
            INSERT INTO review_schema_migrations (version, applied_at)
            VALUES ('legacy-step', '2026-06-24T00:00:00+00:00')
            """
        )
        conn.commit()

    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        columns = {
            row["name"]
            for row in conn.execute("PRAGMA table_info(review_schema_migrations)").fetchall()
        }

    assert "migration_name" in columns
    assert "version" not in columns
    assert set(migration_names(db_path)) == {
        review_db.BASELINE_SCHEMA_MIGRATION,
        "legacy-step",
        "review-file-snapshots-v1",
        "review-model-partition-v1",
        "review-gate-path-v1",
    }


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

    review_db.ensure_db(REPO_ROOT, db_path)

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


def test_snapshot_file_rehydrates_hash_only_snapshot_rows(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    repo = tmp_path / "repo"
    repo.mkdir()
    note = repo / "kb" / "notes" / "sample.md"
    note.parent.mkdir(parents=True)
    note.write_text("rehydrate me\n", encoding="utf-8")

    review_db.ensure_db(REPO_ROOT, db_path)

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

    review_db.ensure_db(REPO_ROOT, db_path)

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
            accepted_note_sha="legacy-note-sha",
            accepted_gate_sha="legacy-gate-sha",
            accepted_at="2026-04-10T10:02:00+02:00",
            acceptance_kind="trivial-change-ack",
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
    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        with pytest.raises(ValueError, match="repo-relative"):
            review_db.snapshot_file(conn, repo_root=repo, path="../outside.md")


def test_rekey_note_path_updates_all_review_tables(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        review_pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/old-note.md",
            gate_id="semantic/internal-consistency",
            model_partition="opus-4-6",
            decision="pass",
            rationale_markdown="ok",
            gate_sha="gate-sha",
            reviewed_note_sha="note-sha",
            reviewed_note_commit="note-commit",
            reviewed_at="2026-04-10T10:01:00+02:00",
        )
        accept_pair(
            conn,
            review_pair_id=review_pair_id,
            note_path="kb/notes/old-note.md",
            gate_id="semantic/internal-consistency",
            model_partition="opus-4-6",
            accepted_note_sha="note-sha",
            accepted_note_commit="note-commit",
            accepted_gate_sha="gate-sha",
            accepted_at="2026-04-10T10:02:00+02:00",
            acceptance_kind="full-review",
        )

        counts = review_db.count_note_path_records(conn, note_path="kb/notes/old-note.md")
        updated = review_db.rekey_note_path(
            conn,
            old_note_path="kb/notes/old-note.md",
            new_note_path="kb/notes/archive/new-note.md",
        )
        conn.commit()

        new_counts = review_db.count_note_path_records(conn, note_path="kb/notes/archive/new-note.md")
        old_counts = review_db.count_note_path_records(conn, note_path="kb/notes/old-note.md")

    assert counts.review_pairs == 1
    assert counts.acceptance_events == 1
    assert updated == counts
    assert new_counts == counts
    assert old_counts.total == 0
