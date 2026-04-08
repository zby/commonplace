from __future__ import annotations

import os
import sqlite3
import subprocess
import sys
from pathlib import Path

from commonplace.review import review_db


REPO_ROOT = Path(__file__).resolve().parents[3]


def test_repair_manual_import_review_results_repairs_decisions_and_footers(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        review_db.insert_gate_review(
            conn,
            review_run_id=None,
            note_path="kb/notes/pass.md",
            gate_id="accessibility/jargon-persistence",
            model_id="test-model",
            decision="warn",
            rationale_markdown="""<!-- REVIEW-METADATA
note-path: kb/notes/pass.md
-->
pass

No jargon-persistence failure detected.

## Result: WARN
""",
            evidence_json=None,
            gate_sha="gate-sha-1",
            reviewed_note_sha="note-sha-1",
            reviewed_note_commit=None,
            reviewed_at="2026-04-05T00:00:00+02:00",
            review_kind="manual-import",
        )
        review_db.insert_gate_review(
            conn,
            review_run_id=None,
            note_path="kb/notes/warn.md",
            gate_id="prose/anthropomorphic-framing",
            model_id="test-model",
            decision="warn",
            rationale_markdown="""## prose/anthropomorphic-framing

**Result: WARN**

One instance to fix.
""",
            evidence_json=None,
            gate_sha="gate-sha-2",
            reviewed_note_sha="note-sha-2",
            reviewed_note_commit=None,
            reviewed_at="2026-04-05T00:00:01+02:00",
            review_kind="manual-import",
        )
        review_db.insert_gate_review(
            conn,
            review_run_id=None,
            note_path="kb/notes/unknown.md",
            gate_id="semantic/internal-consistency",
            model_id="test-model",
            decision="warn",
            rationale_markdown="""### Analysis
Borderline notes without a recoverable legacy decision.

## Result: WARN
""",
            evidence_json=None,
            gate_sha="gate-sha-3",
            reviewed_note_sha="note-sha-3",
            reviewed_note_commit=None,
            reviewed_at="2026-04-05T00:00:02+02:00",
            review_kind="manual-import",
        )
        conn.commit()

    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)
    result = subprocess.run(
        [sys.executable, "-m", "commonplace.review.repair_manual_import_review_results"],
        cwd=REPO_ROOT,
        env=env,
        check=True,
        capture_output=True,
        text=True,
    )

    assert "scanned: 3" in result.stdout
    assert "updated: 2" in result.stdout or "updated: 3" in result.stdout
    assert "inferred_pass: 1" in result.stdout
    assert "inferred_warn: 1" in result.stdout
    assert "inferred_unknown: 1" in result.stdout

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT note_path, decision, rationale_markdown FROM gate_reviews ORDER BY note_path"
        ).fetchall()

    assert rows[0]["note_path"] == "kb/notes/pass.md"
    assert rows[0]["decision"] == "pass"
    assert rows[0]["rationale_markdown"].rstrip().endswith("## Result: PASS")

    assert rows[1]["note_path"] == "kb/notes/unknown.md"
    assert rows[1]["decision"] == "unknown"
    assert rows[1]["rationale_markdown"].rstrip().endswith("## Result: UNKNOWN")

    assert rows[2]["note_path"] == "kb/notes/warn.md"
    assert rows[2]["decision"] == "warn"
    assert rows[2]["rationale_markdown"].rstrip().endswith("## Result: WARN")
    assert "**Result: WARN**" not in rows[2]["rationale_markdown"]
