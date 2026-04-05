from __future__ import annotations

import importlib.util
import sqlite3
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


review_db = load_module("review_db_schema_test", SCRIPTS_DIR / "review_db.py")


def test_ensure_db_upgrades_acceptance_events_to_support_gate_migration(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    schema_text = (SCRIPTS_DIR / "review-schema.sql").read_text(encoding="utf-8")
    old_schema = schema_text.replace("            'gate-migration',\n", "")

    with sqlite3.connect(db_path) as conn:
        conn.executescript(old_schema)
        conn.execute(
            """
            INSERT INTO acceptance_events (
                note_path,
                gate_id,
                model_id,
                accepted_review_id,
                accepted_note_sha,
                accepted_note_commit,
                accepted_gate_sha,
                accepted_at,
                acceptance_kind
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "kb/notes/sample.md",
                "prose/source-residue",
                "test-model",
                None,
                "note-sha-1",
                "commit-1",
                "gate-sha-1",
                "2026-04-05T12:00:00+00:00",
                "trivial-change-ack",
            ),
        )
        conn.commit()

    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/sample.md",
            gate_id="prose/source-residue",
            model_id="test-model",
            accepted_review_id=None,
            accepted_note_sha="note-sha-1",
            accepted_note_commit="commit-1",
            accepted_gate_sha="gate-sha-2",
            accepted_at="2026-04-05T12:05:00+00:00",
            acceptance_kind="gate-migration",
        )
        conn.commit()

        row = conn.execute(
            """
            SELECT accepted_gate_sha, acceptance_kind
            FROM current_gate_acceptances
            WHERE note_path = ? AND gate_id = ? AND model_id = ?
            """,
            ("kb/notes/sample.md", "prose/source-residue", "test-model"),
        ).fetchone()

    assert row is not None
    assert row["accepted_gate_sha"] == "gate-sha-2"
    assert row["acceptance_kind"] == "gate-migration"
