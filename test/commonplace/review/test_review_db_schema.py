from __future__ import annotations

from hashlib import sha256
from importlib import resources
import sqlite3
from pathlib import Path

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


def table_columns(db_path: Path, table_name: str) -> set[str]:
    with review_db.connect(db_path) as conn:
        rows = conn.execute(f"PRAGMA table_info({table_name})").fetchall()
    return {row["name"] for row in rows}


def view_columns(db_path: Path, view_name: str) -> set[str]:
    with review_db.connect(db_path) as conn:
        rows = conn.execute(f"PRAGMA table_info({view_name})").fetchall()
    return {row["name"] for row in rows}


def test_ensure_db_initializes_new_db_from_current_schema(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"

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
    assert "'gate-migration'" in row["sql"].lower()
    assert set(migration_names(db_path)) == {
        review_db.BASELINE_SCHEMA_MIGRATION,
        "review-file-snapshots-v1",
    }
    assert table_columns(db_path, "review_file_snapshots") == {
        "snapshot_id",
        "path",
        "content_sha256",
        "content_text",
        "captured_at",
    }
    assert {
        "reviewed_note_snapshot_id",
        "reviewed_gate_snapshot_id",
    }.issubset(table_columns(db_path, "review_pairs"))
    assert {
        "accepted_note_snapshot_id",
        "accepted_gate_snapshot_id",
    }.issubset(table_columns(db_path, "acceptance_events"))
    assert {
        "accepted_note_snapshot_id",
        "accepted_gate_snapshot_id",
        "accepted_note_hash",
        "accepted_gate_hash",
    }.issubset(view_columns(db_path, "current_gate_acceptances"))


def test_ensure_db_migrates_existing_db_to_review_file_snapshots(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    schema_text = (resources.files("commonplace.review") / "review-schema.sql").read_text(encoding="utf-8")

    with sqlite3.connect(db_path) as conn:
        conn.executescript(schema_text)
        conn.execute(
            """
            DELETE FROM review_schema_migrations
            WHERE migration_name = 'review-file-snapshots-v1'
            """
        )
        conn.commit()

    review_db.ensure_db(REPO_ROOT, db_path)

    assert "review-file-snapshots-v1" in migration_names(db_path)
    assert "review_file_snapshots" in {
        row[0]
        for row in sqlite3.connect(db_path).execute(
            "SELECT name FROM sqlite_master WHERE type = 'table'"
        ).fetchall()
    }
    assert "accepted_note_hash" in view_columns(db_path, "stale_gate_pairs")


def test_ensure_db_applies_pending_schema_migrations_once(tmp_path: Path, monkeypatch) -> None:
    db_path = tmp_path / "review-store.sqlite"

    def apply_probe_migration(conn: sqlite3.Connection) -> None:
        conn.execute("CREATE TABLE migration_probe (value TEXT NOT NULL)")
        conn.execute("INSERT INTO migration_probe (value) VALUES ('applied')")

    monkeypatch.setattr(
        review_db,
        "SCHEMA_MIGRATIONS",
        (review_db.SchemaMigration("999-test-probe", apply_probe_migration),),
    )

    review_db.ensure_db(REPO_ROOT, db_path)
    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        probe_rows = conn.execute("SELECT value FROM migration_probe").fetchall()

    assert [row["value"] for row in probe_rows] == ["applied"]
    assert set(migration_names(db_path)) == {review_db.BASELINE_SCHEMA_MIGRATION, "999-test-probe"}


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


def test_snapshot_file_rejects_non_repo_relative_paths(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    repo = tmp_path / "repo"
    repo.mkdir()
    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        try:
            review_db.snapshot_file(conn, repo_root=repo, path="../outside.md")
        except ValueError as exc:
            assert "repo-relative" in str(exc)
        else:
            raise AssertionError("expected ValueError")


def test_rekey_note_path_updates_all_review_tables(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        review_pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/old-note.md",
            gate_id="semantic/internal-consistency",
            model_id="opus-4-6",
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
            model_id="opus-4-6",
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
