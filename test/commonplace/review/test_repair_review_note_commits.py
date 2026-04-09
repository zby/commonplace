from __future__ import annotations

import os
import sqlite3
import subprocess
import sys
from pathlib import Path

from commonplace.review import review_db, review_metadata


REPO_ROOT = Path(__file__).resolve().parents[3]
TEST_MODEL = "test-model"


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def make_note(path: Path, title: str, body: str) -> Path:
    return write(
        path,
        f"""---
description: Test note
type: note
traits: []
status: current
---

# {title}
{body}
""",
    )


def make_gate(path: Path, gate_id: str) -> Path:
    return write(
        path,
        f"""---
gate_id: {gate_id}
name: Test gate
lens: prose
watches: [body]
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


def commit_all(path: Path, message: str, *, date: str) -> str:
    subprocess.run(["git", "add", "."], cwd=path, check=True, capture_output=True)
    env = os.environ.copy()
    env["GIT_COMMITTER_DATE"] = date
    env["GIT_AUTHOR_DATE"] = date
    subprocess.run(["git", "commit", "-m", message], cwd=path, check=True, capture_output=True, env=env)
    return subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=path,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def test_repair_review_note_commits_backfills_before_after_and_leaves_unresolved(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    init_repo(repo)

    gate = make_gate(
        repo / "kb" / "instructions" / "review-gates" / "prose" / "source-residue.md",
        "prose/source-residue",
    )
    gate_sha = review_metadata.git_blob_sha(gate)

    before_note = make_note(repo / "kb" / "notes" / "before.md", "Before", "\nFirst version.\n")
    before_commit = commit_all(repo, "before v1", date="2026-04-04T10:00:00+00:00")
    before_sha = review_metadata.git_blob_sha(before_note)
    make_note(before_note, "Before", "\nSecond version.\n")
    commit_all(repo, "before v2", date="2026-04-04T12:00:00+00:00")

    after_note = make_note(repo / "kb" / "notes" / "after.md", "After", "\nFirst version.\n")
    commit_all(repo, "after v1", date="2026-04-05T10:00:00+00:00")
    make_note(after_note, "After", "\nSecond version.\n")
    after_commit = commit_all(repo, "after v2", date="2026-04-05T12:00:00+00:00")
    after_sha = review_metadata.git_blob_sha(after_note)

    unresolved_note = make_note(repo / "kb" / "notes" / "unresolved.md", "Unresolved", "\nFirst version.\n")
    commit_all(repo, "unresolved v1", date="2026-04-06T10:00:00+00:00")
    make_note(unresolved_note, "Unresolved", "\nSecond version.\n")
    commit_all(repo, "unresolved v2", date="2026-04-06T12:00:00+00:00")

    db_path = repo / "kb" / "reports" / "review-store.sqlite"
    review_db.ensure_db(repo, db_path)

    with review_db.connect(db_path) as conn:
        before_run = review_db.insert_review_run(
            conn,
            note_path="kb/notes/before.md",
            model_id=TEST_MODEL,
            runner="codex",
            reviewed_note_sha=before_sha,
            reviewed_note_commit=None,
            started_at="2026-04-04T11:00:00+00:00",
            completed_at="2026-04-04T11:05:00+00:00",
            status="completed",
        )
        before_review = review_db.insert_gate_review(
            conn,
            review_run_id=before_run,
            note_path="kb/notes/before.md",
            gate_id="prose/source-residue",
            model_id=TEST_MODEL,
            decision="pass",
            rationale_markdown="Looks good.\n\n## Result: PASS\n",
            evidence_json=None,
            gate_sha=gate_sha,
            reviewed_note_sha=before_sha,
            reviewed_note_commit=None,
            reviewed_at="2026-04-04T11:05:00+00:00",
            review_kind="full-review",
        )
        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/before.md",
            gate_id="prose/source-residue",
            model_id=TEST_MODEL,
            accepted_review_id=before_review,
            accepted_note_sha=before_sha,
            accepted_note_commit=None,
            accepted_gate_sha=gate_sha,
            accepted_at="2026-04-04T11:05:00+00:00",
            acceptance_kind="full-review",
        )

        after_run = review_db.insert_review_run(
            conn,
            note_path="kb/notes/after.md",
            model_id=TEST_MODEL,
            runner="codex",
            reviewed_note_sha=after_sha,
            reviewed_note_commit=None,
            started_at="2026-04-05T11:00:00+00:00",
            completed_at="2026-04-05T11:05:00+00:00",
            status="completed",
        )
        after_review = review_db.insert_gate_review(
            conn,
            review_run_id=after_run,
            note_path="kb/notes/after.md",
            gate_id="prose/source-residue",
            model_id=TEST_MODEL,
            decision="pass",
            rationale_markdown="Looks good.\n\n## Result: PASS\n",
            evidence_json=None,
            gate_sha=gate_sha,
            reviewed_note_sha=after_sha,
            reviewed_note_commit=None,
            reviewed_at="2026-04-05T11:05:00+00:00",
            review_kind="full-review",
        )
        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/after.md",
            gate_id="prose/source-residue",
            model_id=TEST_MODEL,
            accepted_review_id=after_review,
            accepted_note_sha=after_sha,
            accepted_note_commit=None,
            accepted_gate_sha=gate_sha,
            accepted_at="2026-04-05T11:05:00+00:00",
            acceptance_kind="full-review",
        )

        unresolved_run = review_db.insert_review_run(
            conn,
            note_path="kb/notes/unresolved.md",
            model_id=TEST_MODEL,
            runner="codex",
            reviewed_note_sha="missing-note-sha",
            reviewed_note_commit=None,
            started_at="2026-04-06T11:00:00+00:00",
            completed_at="2026-04-06T11:05:00+00:00",
            status="completed",
        )
        unresolved_review = review_db.insert_gate_review(
            conn,
            review_run_id=unresolved_run,
            note_path="kb/notes/unresolved.md",
            gate_id="prose/source-residue",
            model_id=TEST_MODEL,
            decision="pass",
            rationale_markdown="Looks good.\n\n## Result: PASS\n",
            evidence_json=None,
            gate_sha=gate_sha,
            reviewed_note_sha="missing-note-sha",
            reviewed_note_commit=None,
            reviewed_at="2026-04-06T11:05:00+00:00",
            review_kind="full-review",
        )
        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/unresolved.md",
            gate_id="prose/source-residue",
            model_id=TEST_MODEL,
            accepted_review_id=unresolved_review,
            accepted_note_sha="missing-note-sha",
            accepted_note_commit=None,
            accepted_gate_sha=gate_sha,
            accepted_at="2026-04-06T11:05:00+00:00",
            acceptance_kind="full-review",
        )
        conn.commit()

    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)
    result = subprocess.run(
        [sys.executable, "-m", "commonplace.review.repair_review_note_commits"],
        cwd=repo,
        env=env,
        check=True,
        capture_output=True,
        text=True,
    )

    assert "review_runs_scanned: 3" in result.stdout
    assert "review_runs_updated: 2" in result.stdout
    assert "gate_reviews_scanned: 3" in result.stdout
    assert "gate_reviews_updated: 2" in result.stdout
    assert "acceptance_events_scanned: 3" in result.stdout
    assert "acceptance_events_updated: 2" in result.stdout
    assert "matched_before: 3" in result.stdout
    assert "matched_after: 3" in result.stdout
    assert "unresolved: 3" in result.stdout

    with sqlite3.connect(db_path) as conn:
        before_row = conn.execute(
            "SELECT reviewed_note_commit FROM review_runs WHERE note_path = ?",
            ("kb/notes/before.md",),
        ).fetchone()
        assert before_row is not None
        assert before_row[0] == before_commit

        after_row = conn.execute(
            "SELECT reviewed_note_commit FROM review_runs WHERE note_path = ?",
            ("kb/notes/after.md",),
        ).fetchone()
        assert after_row is not None
        assert after_row[0] == after_commit

        unresolved_row = conn.execute(
            "SELECT reviewed_note_commit FROM review_runs WHERE note_path = ?",
            ("kb/notes/unresolved.md",),
        ).fetchone()
        assert unresolved_row is not None
        assert unresolved_row[0] is None

        before_gate = conn.execute(
            "SELECT reviewed_note_commit FROM gate_reviews WHERE note_path = ?",
            ("kb/notes/before.md",),
        ).fetchone()
        assert before_gate is not None
        assert before_gate[0] == before_commit

        after_acceptance = conn.execute(
            "SELECT accepted_note_commit FROM acceptance_events WHERE note_path = ?",
            ("kb/notes/after.md",),
        ).fetchone()
        assert after_acceptance is not None
        assert after_acceptance[0] == after_commit
