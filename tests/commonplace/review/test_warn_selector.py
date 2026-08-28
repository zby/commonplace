from __future__ import annotations

import json
from pathlib import Path

import pytest

from commonplace.review import review_db, warn_selector

TEST_MODEL = "test-model"
REVIEWED_AT = "2026-04-01T00:00:00+00:00"
GATE_PATH = "kb/instructions/review-gates/prose/source-residue.md"
ACTIONABLE_WARN_REVIEW = "### Findings\n- WARN: actionable finding\n"


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def make_note(path: Path, *, body: str = "Body.") -> Path:
    return write(
        path,
        f"""---
description: Test note
type: kb/types/note.md
traits: []
---

# Test note

{body}
""",
    )


def make_gate(path: Path, extra: str = "") -> Path:
    return write(
        path,
        f"""---
gate_id: prose/source-residue
name: Source Residue
lens: prose
watches: [body]
staleness: changed
---

## Failure mode

Fixture gate.
{extra}
""",
    )


def seed_review(
    repo: Path,
    db_path: Path,
    *,
    outcome: str = "warn",
    review_text: str = ACTIONABLE_WARN_REVIEW + "\n## Result: WARN\n",
) -> Path:
    review_db.ensure_db(db_path)
    with review_db.connect(db_path) as conn:
        note_snapshot = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/sample.md")
        criterion_snapshot = review_db.snapshot_file(conn, repo_root=repo, path=GATE_PATH)
        review_job_id = review_db.create_job_with_pairs(
            conn,
            model_partition=TEST_MODEL,
            runner="test-runner",
            created_at=REVIEWED_AT,
            status="queued",
            grouping="note",
            pairs=[
                review_db.ReviewPairRequest(
                    note_path="kb/notes/sample.md",
                    criterion_path=GATE_PATH,
                    pair_ordinal=1,
                    result_kind="verdict",
                    reviewed_note_snapshot_id=note_snapshot.snapshot_id,
                    reviewed_criterion_snapshot_id=criterion_snapshot.snapshot_id,
                )
            ],
        )
        review_db.complete_review_pairs(
            conn,
            review_job_id=review_job_id,
            review_pairs=[
                review_db.ReviewPairCompletion(
                    note_path="kb/notes/sample.md",
                    criterion_path=GATE_PATH,
                    outcome=outcome,
                    completed_at=REVIEWED_AT,
                )
            ],
            completed_at=REVIEWED_AT,
        )
        review_db.complete_review_job(conn, review_job_id=review_job_id, completed_at=REVIEWED_AT)
        review_pair = review_db.load_review_pairs_for_job(conn, review_job_id=review_job_id)[0]
        assert review_pair.result_path is not None
        write(repo / review_pair.result_path, review_text)
        review_db.upsert_freshness_baseline(
            conn,
            note_path="kb/notes/sample.md",
            criterion_path=GATE_PATH,
            model_partition=TEST_MODEL,
            evidence_review_pair_id=review_pair.review_pair_id,
            baseline_note_snapshot_id=note_snapshot.snapshot_id,
            baseline_criterion_snapshot_id=criterion_snapshot.snapshot_id,
            baseline_updated_at=REVIEWED_AT,
        )
        conn.commit()
    return repo / review_pair.result_path


def test_warn_selector_uses_criterion_snapshot_hash_without_git(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    make_note(repo / "kb" / "notes" / "sample.md")
    make_gate(repo / GATE_PATH)
    db_path = repo / "kb" / "reports" / "commonplace-store.sqlite"
    seed_review(repo, db_path)

    notes, stale_pairs = warn_selector.scan_reviews(repo, db_path=db_path)

    assert stale_pairs == []
    assert len(notes) == 1
    assert notes[0].note_path == "kb/notes/sample.md"
    assert notes[0].warns[0].warn_text == "actionable finding"


def test_warn_selector_skips_warns_when_snapshot_gate_changed(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    make_note(repo / "kb" / "notes" / "sample.md")
    gate = make_gate(repo / GATE_PATH)
    db_path = repo / "kb" / "reports" / "commonplace-store.sqlite"
    seed_review(repo, db_path)
    make_gate(gate, extra="\nChanged gate text.\n")

    notes, stale_pairs = warn_selector.scan_reviews(repo, db_path=db_path)

    assert notes == []
    assert [
        (pair.note_path, pair.criterion_path, pair.model_partition, pair.reasons)
        for pair in stale_pairs
    ] == [
        (
            "kb/notes/sample.md",
            GATE_PATH,
            TEST_MODEL,
            ("criterion-changed",),
        )
    ]


def test_warn_selector_reports_note_changed_residue_outside_queue(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    note = make_note(repo / "kb" / "notes" / "sample.md")
    make_gate(repo / GATE_PATH)
    db_path = repo / "kb" / "reports" / "commonplace-store.sqlite"
    seed_review(repo, db_path)
    make_note(note, body="Changed body.")

    notes, stale_pairs = warn_selector.scan_reviews(repo, db_path=db_path)

    assert notes == []
    assert len(stale_pairs) == 1
    stale_pair = stale_pairs[0]
    assert stale_pair.note_path == "kb/notes/sample.md"
    assert stale_pair.criterion_path == GATE_PATH
    assert stale_pair.model_partition == TEST_MODEL
    assert stale_pair.reasons == ("note-changed",)
    assert json.loads(warn_selector.render_json(notes, stale_pairs)) == [
        {
            "stale_pairs": [
                {
                    "note_path": "kb/notes/sample.md",
                    "criterion_path": GATE_PATH,
                    "model_partition": TEST_MODEL,
                    "review_pair_id": stale_pair.review_pair_id,
                    "reasons": ["note-changed"],
                }
            ]
        }
    ]
    assert "stale warn review pair(s) skipped" in warn_selector.render_grouped(
        notes,
        stale_pairs,
    )


@pytest.mark.parametrize("outcome", ["pass", "fail"])
def test_warn_selector_skips_explicit_warns_from_non_warn_pairs(
    tmp_path: Path,
    outcome: str,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    make_note(repo / "kb" / "notes" / "sample.md")
    make_gate(repo / GATE_PATH)
    db_path = repo / "kb" / "reports" / "commonplace-store.sqlite"
    seed_review(
        repo,
        db_path,
        outcome=outcome,
        review_text=ACTIONABLE_WARN_REVIEW + f"\n## Result: {outcome.upper()}\n",
    )
    make_note(repo / "kb" / "notes" / "sample.md", body="Changed body.")

    notes, stale_pairs = warn_selector.scan_reviews(repo, db_path=db_path)

    assert notes == []
    assert stale_pairs == []
