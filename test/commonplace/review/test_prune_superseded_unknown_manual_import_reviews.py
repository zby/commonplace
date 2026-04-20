from __future__ import annotations

import sqlite3
from pathlib import Path

from commonplace.review import review_db

from ._run_cli import run_cli


REPO_ROOT = Path(__file__).resolve().parents[3]


def test_prune_superseded_unknown_manual_import_reviews_deletes_only_superseded_rows(
    tmp_path: Path,
) -> None:
    db_path = tmp_path / "review-store.sqlite"
    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        old_full_review_replaced = review_db.insert_gate_review(
            conn,
            review_run_id=None,
            note_path="kb/notes/one.md",
            gate_id="semantic/grounding-alignment",
            model_id="test-model",
            decision="unknown",
            rationale_markdown="Legacy import\n\n## Result: UNKNOWN\n",
            evidence_json=None,
            gate_sha="gate-sha-1",
            reviewed_note_sha="note-sha-1a",
            reviewed_note_commit=None,
            reviewed_at="2026-04-05T00:00:00+02:00",
            review_kind="manual-import",
        )
        new_full_review = review_db.insert_gate_review(
            conn,
            review_run_id=None,
            note_path="kb/notes/one.md",
            gate_id="semantic/grounding-alignment",
            model_id="test-model",
            decision="pass",
            rationale_markdown="Fresh review\n\n## Result: PASS\n",
            evidence_json=None,
            gate_sha="gate-sha-1",
            reviewed_note_sha="note-sha-1b",
            reviewed_note_commit=None,
            reviewed_at="2026-04-05T00:01:00+02:00",
            review_kind="full-review",
        )
        old_manual_import_replaced = review_db.insert_gate_review(
            conn,
            review_run_id=None,
            note_path="kb/notes/two.md",
            gate_id="prose/source-residue",
            model_id="test-model",
            decision="unknown",
            rationale_markdown="Legacy import A\n\n## Result: UNKNOWN\n",
            evidence_json=None,
            gate_sha="gate-sha-2",
            reviewed_note_sha="note-sha-2a",
            reviewed_note_commit=None,
            reviewed_at="2026-04-05T00:02:00+02:00",
            review_kind="manual-import",
        )
        new_manual_import = review_db.insert_gate_review(
            conn,
            review_run_id=None,
            note_path="kb/notes/two.md",
            gate_id="prose/source-residue",
            model_id="test-model",
            decision="unknown",
            rationale_markdown="Legacy import B\n\n## Result: UNKNOWN\n",
            evidence_json=None,
            gate_sha="gate-sha-2",
            reviewed_note_sha="note-sha-2b",
            reviewed_note_commit=None,
            reviewed_at="2026-04-05T00:03:00+02:00",
            review_kind="manual-import",
        )
        current_unknown = review_db.insert_gate_review(
            conn,
            review_run_id=None,
            note_path="kb/notes/three.md",
            gate_id="accessibility/undefined-terms",
            model_id="test-model",
            decision="unknown",
            rationale_markdown="Still current\n\n## Result: UNKNOWN\n",
            evidence_json=None,
            gate_sha="gate-sha-3",
            reviewed_note_sha="note-sha-3a",
            reviewed_note_commit=None,
            reviewed_at="2026-04-05T00:04:00+02:00",
            review_kind="manual-import",
        )

        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/one.md",
            gate_id="semantic/grounding-alignment",
            model_id="test-model",
            accepted_review_id=old_full_review_replaced,
            accepted_note_sha="note-sha-1a",
            accepted_note_commit=None,
            accepted_gate_sha="gate-sha-1",
            accepted_at="2026-04-05T00:00:10+02:00",
            acceptance_kind="migration-import",
        )
        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/one.md",
            gate_id="semantic/grounding-alignment",
            model_id="test-model",
            accepted_review_id=new_full_review,
            accepted_note_sha="note-sha-1b",
            accepted_note_commit=None,
            accepted_gate_sha="gate-sha-1",
            accepted_at="2026-04-05T00:01:10+02:00",
            acceptance_kind="full-review",
        )

        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/two.md",
            gate_id="prose/source-residue",
            model_id="test-model",
            accepted_review_id=old_manual_import_replaced,
            accepted_note_sha="note-sha-2a",
            accepted_note_commit=None,
            accepted_gate_sha="gate-sha-2",
            accepted_at="2026-04-05T00:02:10+02:00",
            acceptance_kind="migration-import",
        )
        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/two.md",
            gate_id="prose/source-residue",
            model_id="test-model",
            accepted_review_id=new_manual_import,
            accepted_note_sha="note-sha-2b",
            accepted_note_commit=None,
            accepted_gate_sha="gate-sha-2",
            accepted_at="2026-04-05T00:03:10+02:00",
            acceptance_kind="migration-import",
        )

        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/three.md",
            gate_id="accessibility/undefined-terms",
            model_id="test-model",
            accepted_review_id=current_unknown,
            accepted_note_sha="note-sha-3a",
            accepted_note_commit=None,
            accepted_gate_sha="gate-sha-3",
            accepted_at="2026-04-05T00:04:10+02:00",
            acceptance_kind="migration-import",
        )
        conn.commit()

    result = run_cli(
        "prune_superseded_unknown_manual_import_reviews",
        cwd=REPO_ROOT,
        db_path=db_path,
    )

    assert "target_rows: 2" in result.stdout
    assert "historical_acceptance_refs: 2" in result.stdout
    assert "replaced_by_full_review: 1" in result.stdout
    assert "replaced_by_manual_import: 1" in result.stdout
    assert "deleted: 2" in result.stdout

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        remaining_ids = {
            int(row["id"])
            for row in conn.execute("SELECT id FROM gate_reviews ORDER BY id").fetchall()
        }
        acceptance_rows = conn.execute(
            """
            SELECT note_path, gate_id, accepted_review_id
            FROM acceptance_events
            ORDER BY id
            """
        ).fetchall()

    assert old_full_review_replaced not in remaining_ids
    assert old_manual_import_replaced not in remaining_ids
    assert new_full_review in remaining_ids
    assert new_manual_import in remaining_ids
    assert current_unknown in remaining_ids

    assert acceptance_rows[0]["accepted_review_id"] is None
    assert acceptance_rows[1]["accepted_review_id"] == new_full_review
    assert acceptance_rows[2]["accepted_review_id"] is None
    assert acceptance_rows[3]["accepted_review_id"] == new_manual_import
    assert acceptance_rows[4]["accepted_review_id"] == current_unknown
