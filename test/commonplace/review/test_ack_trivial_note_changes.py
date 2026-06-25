from __future__ import annotations

import os
import sqlite3
import subprocess
from pathlib import Path

from commonplace.review import ack_trivial_note_changes, review_db, review_metadata, review_target_selector
from commonplace.review.ack_trivial_note_changes import qualifying_pairs
from commonplace.review.review_target_selector import ack_pairs
from test.commonplace.review.pair_helpers import accept_pair, insert_completed_pair


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


def init_repo(path: Path) -> None:
    subprocess.run(["git", "init"], cwd=path, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.name", "Test User"], cwd=path, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=path, check=True, capture_output=True)


def commit_all(path: Path, message: str, *, date: str | None = None) -> str:
    subprocess.run(["git", "add", "."], cwd=path, check=True, capture_output=True)
    env = os.environ.copy()
    if date is not None:
        env["GIT_COMMITTER_DATE"] = date
        env["GIT_AUTHOR_DATE"] = date
    subprocess.run(["git", "commit", "-m", message], cwd=path, check=True, capture_output=True, env=env)
    result = subprocess.run(["git", "rev-parse", "HEAD"], cwd=path, check=True, capture_output=True, text=True)
    return result.stdout.strip()


def build_fixture(
    tmp_path: Path,
    *,
    gate_id: str = "prose/source-residue",
    lens: str = "prose",
    watches: str = "[body]",
) -> tuple[Path, Path]:
    """Commit one note + one gate; seed DB with a full-review acceptance for that pair."""
    repo = tmp_path / "repo"
    repo.mkdir()
    init_repo(repo)

    note = make_note(repo / "kb" / "notes" / "sample.md", "\nBody.\n")
    gate = make_gate(
        repo / "kb" / "instructions" / "review-gates" / lens / f"{gate_id.split('/', 1)[1]}.md",
        gate_id,
        lens=lens,
        watches=watches,
    )
    commit = commit_all(repo, "initial fixture")

    note_sha = review_metadata.git_blob_sha(note)
    gate_sha = review_metadata.git_blob_sha(gate)

    db_path = repo / "kb" / "reports" / "review-store.sqlite"
    review_db.ensure_db(repo, db_path)
    with review_db.connect(db_path) as conn:
        review_pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/sample.md",
            gate_id=gate_id,
            model_partition=TEST_MODEL,
            decision="pass",
            rationale_markdown="Looks good.\n\n## Result: PASS\n",
            gate_sha=gate_sha,
            reviewed_note_sha=note_sha,
            reviewed_note_commit=commit,
            reviewed_at="2026-04-01T00:00:00+00:00",
            review_kind="full-review",
        )
        accept_pair(
            conn,
            review_pair_id=review_pair_id,
            note_path="kb/notes/sample.md",
            gate_id=gate_id,
            model_partition=TEST_MODEL,
            accepted_note_sha=note_sha,
            accepted_note_commit=commit,
            accepted_gate_sha=gate_sha,
            accepted_at="2026-04-01T00:00:00+00:00",
            acceptance_kind="full-review",
        )
        conn.commit()

    return repo, db_path


def seed_snapshot_review(repo: Path, db_path: Path, *, note_path: str, gate_path: str) -> None:
    review_db.ensure_db(repo, db_path)
    with review_db.connect(db_path) as conn:
        note_snapshot = review_db.snapshot_file(conn, repo_root=repo, path=note_path)
        gate_snapshot = review_db.snapshot_file(conn, repo_root=repo, path=gate_path)
        review_run_id = review_db.create_run_with_pairs(
            conn,
            model_partition=TEST_MODEL,
            runner="test-runner",
            started_at="2026-04-01T00:00:00+00:00",
            packing="note",
            pairs=[
                review_db.ReviewPairRequest(
                    note_path=note_path,
                    gate_path=gate_path,
                    gate_sha="legacy-gate-sha",
                    reviewed_note_sha="legacy-note-sha",
                    reviewed_note_commit=None,
                    reviewed_note_snapshot_id=note_snapshot.snapshot_id,
                    reviewed_gate_snapshot_id=gate_snapshot.snapshot_id,
                    pair_ordinal=0,
                )
            ],
        )
        review_db.complete_review_pairs(
            conn,
            review_run_id=review_run_id,
            review_pairs=[
                review_db.PendingReviewPair(
                    note_path=note_path,
                    gate_path=gate_path,
                    decision="pass",
                    rationale_markdown="Looks good.\n\n## Result: PASS\n",
                    reviewed_at="2026-04-01T00:00:00+00:00",
                )
            ],
            reviewed_at="2026-04-01T00:00:00+00:00",
        )
        review_pair = review_db.load_review_pairs_for_run(conn, review_run_id=review_run_id)[0]
        review_db.append_acceptance_event(
            conn,
            note_path=note_path,
            gate_path=gate_path,
            model_partition=TEST_MODEL,
            accepted_review_pair_id=review_pair.review_pair_id,
            accepted_note_sha="legacy-note-sha",
            accepted_note_commit=None,
            accepted_gate_sha="legacy-gate-sha",
            accepted_note_snapshot_id=note_snapshot.snapshot_id,
            accepted_gate_snapshot_id=gate_snapshot.snapshot_id,
            accepted_at="2026-04-01T00:00:00+00:00",
            acceptance_kind="full-review",
        )
        conn.commit()


# --- Pure-function tests: has_only_unwatched_changes ------------------------


def _note(description: str, traits: str, tags: str, title: str, body: str) -> str:
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


def test_has_only_unwatched_changes_accepts_frontmatter_change_for_body_gate() -> None:
    previous = _note("Test note", "[]", "[]", "Test note", "Body.")
    current = _note("Test note", "[title-as-claim]", "[computational-model]", "Test note", "Body.")

    assert ack_trivial_note_changes.has_only_unwatched_changes(previous, current, watches={"body"})


def test_has_only_unwatched_changes_rejects_body_change_for_body_gate() -> None:
    previous = _note("Test note", "[]", "[]", "Test note", "Body.")
    current = _note("Test note", "[]", "[]", "Test note", "Body changed.")

    assert not ack_trivial_note_changes.has_only_unwatched_changes(previous, current, watches={"body"})


def test_has_only_unwatched_changes_accepts_body_change_for_title_gate() -> None:
    previous = _note("Test note", "[]", "[]", "Test note", "Body.")
    current = _note("Test note", "[]", "[]", "Test note", "Body changed.")

    assert ack_trivial_note_changes.has_only_unwatched_changes(previous, current, watches={"title"})


def test_has_only_unwatched_changes_rejects_title_change_for_title_gate() -> None:
    previous = _note("Test note", "[]", "[]", "Test note", "Body.")
    current = _note("Test note", "[]", "[]", "Updated title", "Body.")

    assert not ack_trivial_note_changes.has_only_unwatched_changes(previous, current, watches={"title"})


def test_has_only_unwatched_changes_rejects_description_change_for_title_description_gate() -> None:
    previous = _note("Test note", "[]", "[]", "Test note", "Body.")
    current = _note("Updated description", "[]", "[]", "Test note", "Body.")

    assert not ack_trivial_note_changes.has_only_unwatched_changes(
        previous, current, watches={"title", "description"}
    )


def test_has_only_unwatched_changes_accepts_tag_change_for_title_description_gate() -> None:
    previous = _note("Test note", "[]", "[]", "Test note", "Body.")
    current = _note("Test note", "[]", "[computational-model]", "Test note", "Body.")

    assert ack_trivial_note_changes.has_only_unwatched_changes(
        previous, current, watches={"title", "description"}
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
                acceptance_kind,
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
    assert row[0] == "trivial-change-ack"
    assert row[1] is not None
    assert row[2] is not None
    assert row[3] is not None
    assert row[4] is not None


def test_qualifying_pairs_uses_snapshot_text_without_git(monkeypatch, tmp_path: Path) -> None:
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
    monkeypatch.setattr(
        review_target_selector,
        "git_blob_sha",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(AssertionError("selector should use snapshot hashes")),
    )
    monkeypatch.setattr(
        ack_trivial_note_changes,
        "file_text_at_provenance",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(AssertionError("ack should use snapshot text")),
    )
    monkeypatch.setattr(
        ack_trivial_note_changes,
        "file_text_at_commit",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(AssertionError("ack should use snapshot text")),
    )

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


def test_qualifying_pairs_recovers_previous_text_from_git_log_when_blob_sha_is_missing(tmp_path: Path) -> None:
    """When the accepted note SHA isn't in the git object store, fall back to the
    first commit touching the note after `accepted_at`."""
    repo = tmp_path / "repo"
    repo.mkdir()
    init_repo(repo)

    note = make_note(repo / "kb" / "notes" / "sample.md", "\nBody.\n")
    gate = make_gate(
        repo / "kb" / "instructions" / "review-gates" / "prose" / "source-residue.md",
        "prose/source-residue",
    )
    commit_all(repo, "initial fixture", date="2026-04-04T09:21:19+02:00")

    gate_sha = review_metadata.git_blob_sha(gate)
    db_path = repo / "kb" / "reports" / "review-store.sqlite"
    review_db.ensure_db(repo, db_path)
    with review_db.connect(db_path) as conn:
        review_pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/sample.md",
            gate_id="prose/source-residue",
            model_partition=TEST_MODEL,
            decision="pass",
            rationale_markdown="Looks good.\n\n## Result: PASS\n",
            gate_sha=gate_sha,
            reviewed_note_sha="missing-blob",
            reviewed_note_commit=None,
            reviewed_at="2026-04-04T08:35:54+02:00",
            review_kind="full-review",
        )
        accept_pair(
            conn,
            review_pair_id=review_pair_id,
            note_path="kb/notes/sample.md",
            gate_id="prose/source-residue",
            model_partition=TEST_MODEL,
            accepted_note_sha="missing-blob",
            accepted_note_commit=None,
            accepted_gate_sha=gate_sha,
            accepted_at="2026-04-04T08:36:13+02:00",
            acceptance_kind="full-review",
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
    assert pairs == ["kb/notes/sample.md:kb/instructions/review-gates/prose/source-residue.md"]
