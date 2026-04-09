from __future__ import annotations

from importlib import resources
import sqlite3
from pathlib import Path

from commonplace.review import review_db


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
