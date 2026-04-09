from __future__ import annotations

import os
import sqlite3
import subprocess
import sys
from pathlib import Path

from commonplace.review import review_db


REPO_ROOT = Path(__file__).resolve().parents[3]


def test_prune_superseded_legacy_precommit_reviews_deletes_only_fully_superseded_rows(
    tmp_path: Path,
) -> None:
    db_path = tmp_path / "review-store.sqlite"
    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        superseded_run = review_db.insert_review_run(
            conn,
            note_path="kb/notes/one.md",
            model_id="test-model",
            runner="test",
            reviewed_note_sha="legacy-run-note-sha",
            reviewed_note_commit=None,
            started_at="2026-04-05T00:00:00+02:00",
            completed_at="2026-04-05T00:00:30+02:00",
            status="completed",
        )
        old_gr_one = review_db.insert_gate_review(
            conn,
            review_run_id=superseded_run,
            note_path="kb/notes/one.md",
            gate_id="gate/a",
            model_id="test-model",
            decision="pass",
            rationale_markdown="old a",
            evidence_json=None,
            gate_sha="gate-sha-a",
            reviewed_note_sha="legacy-note-sha-a",
            reviewed_note_commit=None,
            reviewed_at="2026-04-05T00:00:10+02:00",
            review_kind="full-review",
        )
        old_gr_two = review_db.insert_gate_review(
            conn,
            review_run_id=superseded_run,
            note_path="kb/notes/one.md",
            gate_id="gate/b",
            model_id="test-model",
            decision="pass",
            rationale_markdown="old b",
            evidence_json=None,
            gate_sha="gate-sha-b",
            reviewed_note_sha="legacy-note-sha-b",
            reviewed_note_commit=None,
            reviewed_at="2026-04-05T00:00:11+02:00",
            review_kind="full-review",
        )
        new_gr_one = review_db.insert_gate_review(
            conn,
            review_run_id=None,
            note_path="kb/notes/one.md",
            gate_id="gate/a",
            model_id="test-model",
            decision="pass",
            rationale_markdown="new a",
            evidence_json=None,
            gate_sha="gate-sha-a",
            reviewed_note_sha="committed-note-sha-a",
            reviewed_note_commit="commit-a",
            reviewed_at="2026-04-05T00:01:10+02:00",
            review_kind="full-review",
        )
        new_gr_two = review_db.insert_gate_review(
            conn,
            review_run_id=None,
            note_path="kb/notes/one.md",
            gate_id="gate/b",
            model_id="test-model",
            decision="pass",
            rationale_markdown="new b",
            evidence_json=None,
            gate_sha="gate-sha-b",
            reviewed_note_sha="committed-note-sha-b",
            reviewed_note_commit="commit-b",
            reviewed_at="2026-04-05T00:01:11+02:00",
            review_kind="full-review",
        )

        mixed_run = review_db.insert_review_run(
            conn,
            note_path="kb/notes/two.md",
            model_id="test-model",
            runner="test",
            reviewed_note_sha="legacy-run-note-sha-two",
            reviewed_note_commit=None,
            started_at="2026-04-05T00:02:00+02:00",
            completed_at="2026-04-05T00:02:30+02:00",
            status="completed",
        )
        mixed_old = review_db.insert_gate_review(
            conn,
            review_run_id=mixed_run,
            note_path="kb/notes/two.md",
            gate_id="gate/c",
            model_id="test-model",
            decision="pass",
            rationale_markdown="mixed old",
            evidence_json=None,
            gate_sha="gate-sha-c",
            reviewed_note_sha="legacy-note-sha-c",
            reviewed_note_commit=None,
            reviewed_at="2026-04-05T00:02:10+02:00",
            review_kind="full-review",
        )
        mixed_current = review_db.insert_gate_review(
            conn,
            review_run_id=mixed_run,
            note_path="kb/notes/two.md",
            gate_id="gate/d",
            model_id="test-model",
            decision="pass",
            rationale_markdown="mixed current",
            evidence_json=None,
            gate_sha="gate-sha-d",
            reviewed_note_sha="legacy-note-sha-d",
            reviewed_note_commit=None,
            reviewed_at="2026-04-05T00:02:11+02:00",
            review_kind="full-review",
        )
        mixed_new = review_db.insert_gate_review(
            conn,
            review_run_id=None,
            note_path="kb/notes/two.md",
            gate_id="gate/c",
            model_id="test-model",
            decision="pass",
            rationale_markdown="mixed new",
            evidence_json=None,
            gate_sha="gate-sha-c",
            reviewed_note_sha="committed-note-sha-c",
            reviewed_note_commit="commit-c",
            reviewed_at="2026-04-05T00:03:10+02:00",
            review_kind="full-review",
        )

        current_legacy = review_db.insert_gate_review(
            conn,
            review_run_id=None,
            note_path="kb/notes/three.md",
            gate_id="gate/e",
            model_id="test-model",
            decision="pass",
            rationale_markdown="current legacy",
            evidence_json=None,
            gate_sha="gate-sha-e",
            reviewed_note_sha="legacy-note-sha-e",
            reviewed_note_commit=None,
            reviewed_at="2026-04-05T00:04:10+02:00",
            review_kind="full-review",
        )

        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/one.md",
            gate_id="gate/a",
            model_id="test-model",
            accepted_review_id=old_gr_one,
            accepted_note_sha="legacy-note-sha-a",
            accepted_note_commit=None,
            accepted_gate_sha="gate-sha-a",
            accepted_at="2026-04-05T00:00:20+02:00",
            acceptance_kind="full-review",
        )
        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/one.md",
            gate_id="gate/a",
            model_id="test-model",
            accepted_review_id=new_gr_one,
            accepted_note_sha="committed-note-sha-a",
            accepted_note_commit="commit-a",
            accepted_gate_sha="gate-sha-a",
            accepted_at="2026-04-05T00:01:20+02:00",
            acceptance_kind="full-review",
        )
        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/one.md",
            gate_id="gate/b",
            model_id="test-model",
            accepted_review_id=old_gr_two,
            accepted_note_sha="legacy-note-sha-b",
            accepted_note_commit=None,
            accepted_gate_sha="gate-sha-b",
            accepted_at="2026-04-05T00:00:21+02:00",
            acceptance_kind="full-review",
        )
        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/one.md",
            gate_id="gate/b",
            model_id="test-model",
            accepted_review_id=new_gr_two,
            accepted_note_sha="committed-note-sha-b",
            accepted_note_commit="commit-b",
            accepted_gate_sha="gate-sha-b",
            accepted_at="2026-04-05T00:01:21+02:00",
            acceptance_kind="full-review",
        )
        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/two.md",
            gate_id="gate/c",
            model_id="test-model",
            accepted_review_id=mixed_old,
            accepted_note_sha="legacy-note-sha-c",
            accepted_note_commit=None,
            accepted_gate_sha="gate-sha-c",
            accepted_at="2026-04-05T00:02:20+02:00",
            acceptance_kind="full-review",
        )
        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/two.md",
            gate_id="gate/c",
            model_id="test-model",
            accepted_review_id=mixed_new,
            accepted_note_sha="committed-note-sha-c",
            accepted_note_commit="commit-c",
            accepted_gate_sha="gate-sha-c",
            accepted_at="2026-04-05T00:03:20+02:00",
            acceptance_kind="full-review",
        )
        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/two.md",
            gate_id="gate/d",
            model_id="test-model",
            accepted_review_id=mixed_current,
            accepted_note_sha="legacy-note-sha-d",
            accepted_note_commit=None,
            accepted_gate_sha="gate-sha-d",
            accepted_at="2026-04-05T00:02:21+02:00",
            acceptance_kind="full-review",
        )
        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/three.md",
            gate_id="gate/e",
            model_id="test-model",
            accepted_review_id=current_legacy,
            accepted_note_sha="legacy-note-sha-e",
            accepted_note_commit=None,
            accepted_gate_sha="gate-sha-e",
            accepted_at="2026-04-05T00:04:20+02:00",
            acceptance_kind="full-review",
        )
        conn.commit()

    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)
    result = subprocess.run(
        [sys.executable, "-m", "commonplace.review.prune_superseded_legacy_precommit_reviews"],
        cwd=REPO_ROOT,
        env=env,
        check=True,
        capture_output=True,
        text=True,
    )

    assert "target_acceptance_events: 3" in result.stdout
    assert "target_gate_reviews: 3" in result.stdout
    assert "target_review_runs: 1" in result.stdout
    assert "deleted_acceptance_events: 3" in result.stdout
    assert "deleted_gate_reviews: 3" in result.stdout
    assert "deleted_review_runs: 1" in result.stdout

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        remaining_review_runs = {
            int(row["id"]) for row in conn.execute("SELECT id FROM review_runs").fetchall()
        }
        remaining_gate_reviews = {
            int(row["id"]) for row in conn.execute("SELECT id FROM gate_reviews").fetchall()
        }
        acceptance_rows = conn.execute(
            "SELECT note_path, gate_id, accepted_note_commit, accepted_review_id FROM acceptance_events ORDER BY id"
        ).fetchall()

    assert superseded_run not in remaining_review_runs
    assert mixed_run in remaining_review_runs

    assert old_gr_one not in remaining_gate_reviews
    assert old_gr_two not in remaining_gate_reviews
    assert mixed_old not in remaining_gate_reviews
    assert mixed_current in remaining_gate_reviews
    assert current_legacy in remaining_gate_reviews
    assert new_gr_one in remaining_gate_reviews
    assert new_gr_two in remaining_gate_reviews
    assert mixed_new in remaining_gate_reviews

    remaining_pairs = {
        (row["note_path"], row["gate_id"], row["accepted_note_commit"], row["accepted_review_id"])
        for row in acceptance_rows
    }
    assert ("kb/notes/one.md", "gate/a", None, old_gr_one) not in remaining_pairs
    assert ("kb/notes/one.md", "gate/b", None, old_gr_two) not in remaining_pairs
    assert ("kb/notes/two.md", "gate/c", None, mixed_old) not in remaining_pairs
    assert ("kb/notes/two.md", "gate/d", None, mixed_current) in remaining_pairs
    assert ("kb/notes/three.md", "gate/e", None, current_legacy) in remaining_pairs
