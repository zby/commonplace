from __future__ import annotations

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


def make_note(path: Path) -> Path:
    return write(
        path,
        """---
description: Test note
type: kb/types/note.md
traits: []
---

# Test note

Body.
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
) -> None:
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


@pytest.mark.parametrize("outcome", ["pass", "fail"])
def test_extract_warns_ignores_explicit_warn_for_non_warn_outcome(outcome: str) -> None:
    assert warn_selector.extract_warns(ACTIONABLE_WARN_REVIEW, outcome=outcome) == []


def test_warn_selector_uses_criterion_snapshot_hash_without_git(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    make_note(repo / "kb" / "notes" / "sample.md")
    make_gate(repo / GATE_PATH)
    db_path = repo / "kb" / "reports" / "commonplace-store.sqlite"
    seed_review(repo, db_path)

    notes, stale_gates = warn_selector.scan_reviews(repo, db_path=db_path)

    assert stale_gates == []
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

    notes, stale_gates = warn_selector.scan_reviews(repo, db_path=db_path)

    assert notes == []
    assert stale_gates == [GATE_PATH]


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

    notes, stale_gates = warn_selector.scan_reviews(repo, db_path=db_path)

    assert notes == []
    assert stale_gates == []
