from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from commonplace.review import ack_trivial_note_changes, review_db
from commonplace.review.acknowledgement import ack_pairs
from commonplace.review.ack_trivial_note_changes import qualifying_pairs
from tests.commonplace.review.pair_helpers import accept_pair, insert_completed_pair

from ._run_cli import run_cli


TEST_MODEL = "test-model"


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def make_note(
    path: Path,
    body: str,
    *,
    title: str = "Test note",
    description: str = "Test note",
    traits: str = "[]",
    tags: str = "[]",
    status: str = "current",
) -> Path:
    return write(
        path,
        f"""---
description: {description}
type: kb/types/note.md
traits: {traits}
tags: {tags}
status: {status}
---

# {title}
{body}
""",
    )


def make_gate(path: Path, gate_id: str, *, lens: str = "prose", watches: str = "[body]") -> Path:
    return write(
        path,
        f"""---
gate_id: {gate_id}
name: {path.stem}
lens: {lens}
watches: {watches}
staleness: changed
---

## Failure mode

Fixture gate.

## Test

Fixture test.
""",
    )


def build_fixture(
    tmp_path: Path,
    *,
    gate_id: str = "prose/source-residue",
    lens: str = "prose",
    watches: str = "[body]",
) -> tuple[Path, Path]:
    """Create one note + one gate; seed DB with a full-review acceptance for that pair."""
    repo = tmp_path / "repo"
    repo.mkdir()

    make_note(repo / "kb" / "notes" / "sample.md", "\nBody.\n")
    make_gate(
        repo / "kb" / "instructions" / "review-gates" / lens / f"{gate_id.split('/', 1)[1]}.md",
        gate_id,
        lens=lens,
        watches=watches,
    )

    db_path = repo / "kb" / "reports" / "review-store.sqlite"
    review_db.ensure_db(db_path)
    with review_db.connect(db_path) as conn:
        note_snapshot = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/sample.md")
        gate_snapshot = review_db.snapshot_file(
            conn,
            repo_root=repo,
            path=f"kb/instructions/review-gates/{lens}/{gate_id.split('/', 1)[1]}.md",
        )
        review_pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/sample.md",
            gate_id=gate_id,
            model_partition=TEST_MODEL,
            decision="pass",
            reviewed_note_snapshot_id=note_snapshot.snapshot_id,
            reviewed_gate_snapshot_id=gate_snapshot.snapshot_id,
            reviewed_at="2026-04-01T00:00:00+00:00",
        )
        accept_pair(
            conn,
            review_pair_id=review_pair_id,
            note_path="kb/notes/sample.md",
            gate_id=gate_id,
            model_partition=TEST_MODEL,
            accepted_note_snapshot_id=note_snapshot.snapshot_id,
            accepted_gate_snapshot_id=gate_snapshot.snapshot_id,
            accepted_at="2026-04-01T00:00:00+00:00",
        )
        conn.commit()

    return repo, db_path


def seed_snapshot_review(repo: Path, db_path: Path, *, note_path: str, gate_path: str) -> None:
    review_db.ensure_db(db_path)
    with review_db.connect(db_path) as conn:
        note_snapshot = review_db.snapshot_file(conn, repo_root=repo, path=note_path)
        gate_snapshot = review_db.snapshot_file(conn, repo_root=repo, path=gate_path)
        review_job_id = review_db.create_job_with_pairs(
            conn,
            model_partition=TEST_MODEL,
            runner="test-runner",
            created_at="2026-04-01T00:00:00+00:00",
            status="queued",
            packing="note",
            pairs=[
                review_db.ReviewPairRequest(
                    note_path=note_path,
                    gate_path=gate_path,
                    pair_ordinal=0,
                    reviewed_note_snapshot_id=note_snapshot.snapshot_id,
                    reviewed_gate_snapshot_id=gate_snapshot.snapshot_id,
                )
            ],
        )
        review_db.complete_review_pairs(
            conn,
            review_job_id=review_job_id,
            review_pairs=[
                review_db.ReviewPairCompletion(
                    note_path=note_path,
                    gate_path=gate_path,
                    decision="pass",
                    reviewed_at="2026-04-01T00:00:00+00:00",
                )
            ],
            reviewed_at="2026-04-01T00:00:00+00:00",
        )
        review_db.complete_review_job(
            conn,
            review_job_id=review_job_id,
            completed_at="2026-04-01T00:00:00+00:00",
        )
        review_pair = review_db.load_review_pairs_for_job(conn, review_job_id=review_job_id)[0]
        review_db.upsert_acceptance(
            conn,
            note_path=note_path,
            gate_path=gate_path,
            model_partition=TEST_MODEL,
            accepted_review_pair_id=review_pair.review_pair_id,
            accepted_note_snapshot_id=note_snapshot.snapshot_id,
            accepted_gate_snapshot_id=gate_snapshot.snapshot_id,
            accepted_at="2026-04-01T00:00:00+00:00",
        )
        conn.commit()


# --- Pure-function tests: has_only_unwatched_changes ------------------------


def _note(
    *,
    description: str = "Test note",
    traits: str = "[]",
    tags: str = "[]",
    title: str = "Test note",
    body: str = "Body.",
) -> str:
    return f"""---
description: {description}
type: kb/types/note.md
traits: {traits}
tags: {tags}
status: current
---

# {title}
{body}
"""


@pytest.mark.parametrize(
    ("current_kwargs", "watches", "expected"),
    [
        (
            {"traits": "[title-as-claim]", "tags": "[computational-model]"},
            {"body"},
            True,
        ),
        ({"body": "Body changed."}, {"body"}, False),
        ({"body": "Body changed."}, {"title"}, True),
        ({"title": "Updated title"}, {"title"}, False),
        ({"description": "Updated description"}, {"title", "description"}, False),
        ({"tags": "[computational-model]"}, {"title", "description"}, True),
    ],
)
def test_has_only_unwatched_changes_respects_gate_watch_fields(
    current_kwargs: dict[str, str],
    watches: set[str],
    expected: bool,
) -> None:
    previous = _note()
    current = _note(**current_kwargs)

    assert (
        ack_trivial_note_changes.has_only_unwatched_changes(previous, current, watches=watches)
        is expected
    )


# --- Integration tests: qualifying_pairs + ack_pairs ------------------------


def test_qualifying_pairs_finds_note_with_only_unwatched_changes_and_ack_records_it(tmp_path: Path) -> None:
    repo, db_path = build_fixture(tmp_path)
    note_path = repo / "kb" / "notes" / "sample.md"
    make_note(note_path, "\nBody.\n", traits="[title-as-claim]", tags="[computational-model]")

    pairs = qualifying_pairs(
        repo,
        model=TEST_MODEL,
        gate_ids=["kb/instructions/review-gates/prose/source-residue.md"],
        note_filter=["kb/notes"],
        db_path=db_path,
    )
    assert pairs == ["kb/notes/sample.md:kb/instructions/review-gates/prose/source-residue.md"]

    ack_pairs(repo, pairs, TEST_MODEL, db_path=db_path)

    with sqlite3.connect(db_path) as conn:
        row = conn.execute(
            """
            SELECT
                accepted_review_pair_id,
                accepted_note_snapshot_id,
                accepted_gate_snapshot_id,
                accepted_note_hash,
                accepted_gate_hash
            FROM current_gate_acceptances
            WHERE note_path = ? AND gate_path = ? AND model_partition = ?
            """,
            ("kb/notes/sample.md", "kb/instructions/review-gates/prose/source-residue.md", TEST_MODEL),
        ).fetchone()
    assert row is not None
    assert row[0] is not None
    assert row[1] is not None
    assert row[2] is not None
    assert row[3] is not None
    assert row[4] is not None


def test_ack_trivial_note_changes_cli_writes_non_null_review_pair_id(tmp_path: Path) -> None:
    repo, db_path = build_fixture(tmp_path)
    note_path = repo / "kb" / "notes" / "sample.md"
    make_note(note_path, "\nBody.\n", traits="[title-as-claim]", tags="[computational-model]")

    result = run_cli(
        "ack_trivial_note_changes",
        "prose/source-residue",
        "--note",
        "kb/notes",
        "--model",
        TEST_MODEL,
        cwd=repo,
    )

    assert "acked: kb/notes/sample.md prose/source-residue" in result.stdout
    with sqlite3.connect(db_path) as conn:
        row = conn.execute(
            """
            SELECT accepted_review_pair_id
            FROM current_gate_acceptances
            WHERE note_path = ? AND gate_path = ? AND model_partition = ?
            """,
            ("kb/notes/sample.md", "kb/instructions/review-gates/prose/source-residue.md", TEST_MODEL),
        ).fetchone()
    assert row is not None
    assert row[0] is not None


def test_qualifying_pairs_uses_snapshot_text_without_git(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    note = make_note(repo / "kb" / "notes" / "sample.md", "\nBody.\n")
    make_gate(
        repo / "kb" / "instructions" / "review-gates" / "prose" / "source-residue.md",
        "prose/source-residue",
    )
    db_path = repo / "kb" / "reports" / "review-store.sqlite"
    seed_snapshot_review(
        repo,
        db_path,
        note_path="kb/notes/sample.md",
        gate_path="kb/instructions/review-gates/prose/source-residue.md",
    )
    make_note(note, "\nBody.\n", traits="[title-as-claim]", tags="[computational-model]")

    pairs = qualifying_pairs(
        repo,
        model=TEST_MODEL,
        gate_ids=["kb/instructions/review-gates/prose/source-residue.md"],
        note_filter=["kb/notes"],
        db_path=db_path,
    )

    assert pairs == ["kb/notes/sample.md:kb/instructions/review-gates/prose/source-residue.md"]


def test_qualifying_pairs_excludes_notes_where_watched_parts_changed(tmp_path: Path) -> None:
    repo, db_path = build_fixture(
        tmp_path,
        gate_id="frontmatter/title-body-alignment",
        lens="frontmatter",
        watches="[title, body]",
    )
    note_path = repo / "kb" / "notes" / "sample.md"
    make_note(note_path, "\nBody.\n", title="Updated title", tags="[computational-model]")

    pairs = qualifying_pairs(
        repo,
        model=TEST_MODEL,
        gate_ids=["kb/instructions/review-gates/frontmatter/title-body-alignment.md"],
        note_filter=["kb/notes"],
        db_path=db_path,
    )
    assert pairs == []


def test_qualifying_pairs_skips_rows_without_snapshot_text(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()

    note = make_note(repo / "kb" / "notes" / "sample.md", "\nBody.\n")
    make_gate(
        repo / "kb" / "instructions" / "review-gates" / "prose" / "source-residue.md",
        "prose/source-residue",
    )

    db_path = repo / "kb" / "reports" / "review-store.sqlite"
    review_db.ensure_db(db_path)
    with review_db.connect(db_path) as conn:
        note_snapshot = review_db.snapshot_file(conn, repo_root=repo, path="kb/notes/sample.md")
        gate_snapshot = review_db.snapshot_file(
            conn,
            repo_root=repo,
            path="kb/instructions/review-gates/prose/source-residue.md",
        )
        conn.execute(
            "UPDATE review_file_snapshots SET content_text = NULL WHERE snapshot_id = ?",
            (note_snapshot.snapshot_id,),
        )
        review_pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/sample.md",
            gate_id="prose/source-residue",
            model_partition=TEST_MODEL,
            decision="pass",
            reviewed_note_snapshot_id=note_snapshot.snapshot_id,
            reviewed_gate_snapshot_id=gate_snapshot.snapshot_id,
            reviewed_at="2026-04-04T08:35:54+02:00",
        )
        accept_pair(
            conn,
            review_pair_id=review_pair_id,
            note_path="kb/notes/sample.md",
            gate_id="prose/source-residue",
            model_partition=TEST_MODEL,
            accepted_note_snapshot_id=note_snapshot.snapshot_id,
            accepted_gate_snapshot_id=gate_snapshot.snapshot_id,
            accepted_at="2026-04-04T08:36:13+02:00",
        )
        conn.commit()

    make_note(note, "\nBody.\n", traits="[title-as-claim]")

    pairs = qualifying_pairs(
        repo,
        model=TEST_MODEL,
        gate_ids=["kb/instructions/review-gates/prose/source-residue.md"],
        note_filter=["kb/notes"],
        db_path=db_path,
    )
    assert pairs == []
