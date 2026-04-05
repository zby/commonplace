from __future__ import annotations

import importlib.util
import os
import sqlite3
import subprocess
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


review_db = load_module("review_db_reparse_gate_review_decisions_test", SCRIPTS_DIR / "review_db.py")


def test_reparse_gate_review_decisions_updates_stored_decision(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        review_db.insert_gate_review(
            conn,
            review_run_id=None,
            note_path="kb/notes/sample.md",
            gate_id="structural/bullet-capitalization",
            model_id="test-model",
            decision="warn",
            rationale_markdown="""## Result: WARN

### Findings
- PASS: The title is clear and aligned.
""",
            evidence_json=None,
            gate_sha="gate-sha",
            reviewed_note_sha="note-sha",
            reviewed_note_commit=None,
            reviewed_at="2026-04-04T00:00:00+02:00",
            review_kind="manual-import",
        )
        conn.commit()

    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)
    result = subprocess.run(
        [sys.executable, str(SCRIPTS_DIR / "reparse_gate_review_decisions.py")],
        cwd=REPO_ROOT,
        env=env,
        check=True,
        capture_output=True,
        text=True,
        )

    assert "changed: 1" in result.stdout
    assert "unknown: 1" in result.stdout

    with sqlite3.connect(db_path) as conn:
        row = conn.execute("SELECT decision FROM gate_reviews").fetchone()
        assert row is not None
        assert row[0] == "unknown"


def test_reparse_gate_review_decisions_combined_only_skips_legacy_rows(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        review_run_id = review_db.insert_review_run(
            conn,
            note_path="kb/notes/combined.md",
            model_id="test-model",
            runner="claude-code",
            reviewed_note_sha="combined-note-sha",
            reviewed_note_commit=None,
            started_at="2026-04-04T03:00:00+02:00",
            completed_at="2026-04-04T03:00:05+02:00",
            status="completed",
            raw_bundle_markdown="=== GATE REVIEW START: structural/bullet-capitalization ===",
        )
        review_db.insert_gate_review(
            conn,
            review_run_id=review_run_id,
            note_path="kb/notes/combined.md",
            gate_id="structural/bullet-capitalization",
            model_id="test-model",
            decision="warn",
            rationale_markdown="""## Result: WARN

### Findings
- PASS: The title is clear and aligned.
""",
            evidence_json=None,
            gate_sha="combined-gate-sha",
            reviewed_note_sha="combined-note-sha",
            reviewed_note_commit=None,
            reviewed_at="2026-04-04T03:00:05+02:00",
            review_kind="full-review",
        )
        review_db.insert_gate_review(
            conn,
            review_run_id=None,
            note_path="kb/notes/legacy.md",
            gate_id="structural/bullet-capitalization",
            model_id="test-model",
            decision="warn",
            rationale_markdown="""## Result: WARN

### Findings
- PASS: The title is clear and aligned.
""",
            evidence_json=None,
            gate_sha="legacy-gate-sha",
            reviewed_note_sha="legacy-note-sha",
            reviewed_note_commit=None,
            reviewed_at="2026-04-03T03:00:05+02:00",
            review_kind="manual-import",
        )
        conn.commit()

    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)
    result = subprocess.run(
        [sys.executable, str(SCRIPTS_DIR / "reparse_gate_review_decisions.py"), "--combined-only"],
        cwd=REPO_ROOT,
        env=env,
        check=True,
        capture_output=True,
        text=True,
    )

    assert "scanned: 1" in result.stdout
    assert "changed: 1" in result.stdout

    with sqlite3.connect(db_path) as conn:
        rows = conn.execute("SELECT review_run_id, decision FROM gate_reviews ORDER BY id").fetchall()
        assert rows[0] == (review_run_id, "unknown")
        assert rows[1] == (None, "warn")
