from __future__ import annotations

import os
import sqlite3
import subprocess
import sys
from pathlib import Path

from commonplace.review import ack_trivial_note_changes_lib, review_db, review_metadata


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
type: note
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
    title: str = "Test note",
    description: str = "Test note",
    traits: str = "[]",
    tags: str = "[]",
    status: str = "current",
    gate_id: str = "prose/source-residue",
    lens: str = "prose",
    watches: str = "[body]",
) -> tuple[Path, Path]:
    repo = tmp_path / "repo"
    repo.mkdir()
    init_repo(repo)

    note = make_note(
        repo / "kb" / "notes" / "sample.md",
        "\nBody.\n",
        title=title,
        description=description,
        traits=traits,
        tags=tags,
        status=status,
    )
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
        review_id = review_db.insert_gate_review(
            conn,
            note_path="kb/notes/sample.md",
            gate_id=gate_id,
            model_id=TEST_MODEL,
            decision="pass",
            rationale_markdown="Looks good.\n\n## Result: PASS\n",
            evidence_json=None,
            gate_sha=gate_sha,
            reviewed_note_sha=note_sha,
            reviewed_note_commit=commit,
            reviewed_at="2026-04-01T00:00:00+00:00",
            review_kind="full-review",
        )
        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/sample.md",
            gate_id=gate_id,
            model_id=TEST_MODEL,
            accepted_review_id=review_id,
            accepted_note_sha=note_sha,
            accepted_note_commit=commit,
            accepted_gate_sha=gate_sha,
            accepted_at="2026-04-01T00:00:00+00:00",
            acceptance_kind="full-review",
        )
        conn.commit()

    return repo, db_path


def test_has_only_unwatched_changes_accepts_frontmatter_change_for_body_gate() -> None:
    previous_text = """---
description: Test note
type: note
traits: []
tags: []
status: seedling
---

# Test note
Body.
"""
    current_text = """---
description: Test note
type: note
traits: [title-as-claim]
tags: [computational-model]
status: current
---

# Test note
Body.
"""

    assert ack_trivial_note_changes_lib.has_only_unwatched_changes(
        previous_text,
        current_text,
        watches={"body"},
    )


def test_has_only_unwatched_changes_rejects_body_change_for_body_gate() -> None:
    previous_text = """---
description: Test note
type: note
traits: []
tags: []
status: current
---

# Test note
Body.
"""
    current_text = """---
description: Test note
type: note
traits: []
tags: []
status: current
---

# Test note
Body changed.
"""

    assert not ack_trivial_note_changes_lib.has_only_unwatched_changes(
        previous_text,
        current_text,
        watches={"body"},
    )


def test_has_only_unwatched_changes_accepts_body_change_for_title_gate() -> None:
    previous_text = """---
description: Test note
type: note
traits: []
tags: []
status: current
---

# Test note
Body.
"""
    current_text = """---
description: Test note
type: note
traits: []
tags: []
status: current
---

# Test note
Body changed.
"""

    assert ack_trivial_note_changes_lib.has_only_unwatched_changes(
        previous_text,
        current_text,
        watches={"title"},
    )


def test_has_only_unwatched_changes_rejects_title_change_for_title_gate() -> None:
    previous_text = """---
description: Test note
type: note
traits: []
tags: []
status: current
---

# Test note
Body.
"""
    current_text = """---
description: Test note
type: note
traits: []
tags: []
status: current
---

# Updated title
Body.
"""

    assert not ack_trivial_note_changes_lib.has_only_unwatched_changes(
        previous_text,
        current_text,
        watches={"title"},
    )


def test_has_only_unwatched_changes_rejects_description_change_for_title_description_gate() -> None:
    previous_text = """---
description: Test note
type: note
traits: []
tags: []
status: current
---

# Test note
Body.
"""
    current_text = """---
description: Updated description
type: note
traits: []
tags: []
status: current
---

# Test note
Body.
"""

    assert not ack_trivial_note_changes_lib.has_only_unwatched_changes(
        previous_text,
        current_text,
        watches={"title", "description"},
    )


def test_has_only_unwatched_changes_accepts_tag_change_for_title_description_gate() -> None:
    previous_text = """---
description: Test note
type: note
traits: []
tags: []
status: current
---

# Test note
Body.
"""
    current_text = """---
description: Test note
type: note
traits: []
tags: [computational-model]
status: current
---

# Test note
Body.
"""

    assert ack_trivial_note_changes_lib.has_only_unwatched_changes(
        previous_text,
        current_text,
        watches={"title", "description"},
    )


def test_command_acks_frontmatter_change_for_body_gate(tmp_path: Path) -> None:
    repo, db_path = build_fixture(tmp_path)
    note_path = repo / "kb" / "notes" / "sample.md"
    note_path.write_text(
        """---
description: Test note
type: note
traits: [title-as-claim]
tags: [computational-model]
status: current
---
# Test note
Body.
""",
        encoding="utf-8",
    )
    commit_all(repo, "frontmatter-only note change")

    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "commonplace.review.ack_trivial_note_changes",
            "--model",
            TEST_MODEL,
            "prose",
        ],
        cwd=repo,
        env=env,
        capture_output=True,
        text=True,
        check=True,
    )

    assert "acked: kb/notes/sample.md prose/source-residue" in result.stdout

    with sqlite3.connect(db_path) as conn:
        row = conn.execute(
            """
            SELECT acceptance_kind
            FROM current_gate_acceptances
            WHERE note_path = ? AND gate_id = ? AND model_id = ?
            """,
            ("kb/notes/sample.md", "prose/source-residue", TEST_MODEL),
        ).fetchone()
    assert row is not None
    assert row[0] == "trivial-change-ack"


def test_command_acks_body_change_for_title_only_gate(tmp_path: Path) -> None:
    repo, db_path = build_fixture(
        tmp_path,
        gate_id="frontmatter/title-as-claim",
        lens="frontmatter",
        watches="[title]",
    )
    note_path = repo / "kb" / "notes" / "sample.md"
    note_path.write_text(
        """---
description: Test note
type: note
traits: []
tags: []
status: current
---
# Test note
Body changed.
""",
        encoding="utf-8",
    )
    commit_all(repo, "body-only note change")

    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "commonplace.review.ack_trivial_note_changes",
            "--model",
            TEST_MODEL,
            "frontmatter/title-as-claim",
        ],
        cwd=repo,
        env=env,
        capture_output=True,
        text=True,
        check=True,
    )

    assert "acked: kb/notes/sample.md frontmatter/title-as-claim" in result.stdout


def test_command_does_not_ack_when_watched_parts_changed(tmp_path: Path) -> None:
    repo, db_path = build_fixture(
        tmp_path,
        gate_id="frontmatter/title-body-alignment",
        lens="frontmatter",
        watches="[title, body]",
    )
    note_path = repo / "kb" / "notes" / "sample.md"
    note_path.write_text(
        """---
description: Test note
type: note
traits: []
tags: [computational-model]
status: current
---

# Updated title
Body.
""",
        encoding="utf-8",
    )

    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "commonplace.review.ack_trivial_note_changes",
            "--model",
            TEST_MODEL,
            "frontmatter/title-body-alignment",
        ],
        cwd=repo,
        env=env,
        capture_output=True,
        text=True,
        check=True,
    )

    assert result.stdout.strip() == "No qualifying stale pairs found."


def test_dry_run_prints_pairs_without_acknowledging(tmp_path: Path) -> None:
    repo, db_path = build_fixture(tmp_path)
    note_path = repo / "kb" / "notes" / "sample.md"
    note_path.write_text(
        """---
description: Test note
type: note
traits: [title-as-claim]
tags: [computational-model]
status: current
---
# Test note
Body.
""",
        encoding="utf-8",
    )
    commit_all(repo, "recover previous text fixture")

    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "commonplace.review.ack_trivial_note_changes",
            "--model",
            TEST_MODEL,
            "--dry-run",
            "prose",
        ],
        cwd=repo,
        env=env,
        capture_output=True,
        text=True,
        check=True,
    )

    assert "kb/notes/sample.md:prose/source-residue" in result.stdout
    assert "Would ack 1 stale pair(s)." in result.stdout

    with sqlite3.connect(db_path) as conn:
        row = conn.execute(
            """
            SELECT acceptance_kind
            FROM current_gate_acceptances
            WHERE note_path = ? AND gate_id = ? AND model_id = ?
            """,
            ("kb/notes/sample.md", "prose/source-residue", TEST_MODEL),
        ).fetchone()
    assert row is not None
    assert row[0] == "full-review"


def test_command_recovers_previous_text_from_first_commit_after_acceptance_time(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    init_repo(repo)

    note = make_note(repo / "kb" / "notes" / "sample.md", "\nBody.\n")
    gate = make_gate(repo / "kb" / "instructions" / "review-gates" / "prose" / "source-residue.md", "prose/source-residue")
    commit_all(repo, "initial fixture", date="2026-04-04T09:21:19+02:00")

    gate_sha = review_metadata.git_blob_sha(gate)
    db_path = repo / "kb" / "reports" / "review-store.sqlite"
    review_db.ensure_db(repo, db_path)
    with review_db.connect(db_path) as conn:
        review_id = review_db.insert_gate_review(
            conn,
            note_path="kb/notes/sample.md",
            gate_id="prose/source-residue",
            model_id=TEST_MODEL,
            decision="pass",
            rationale_markdown="Looks good.\n\n## Result: PASS\n",
            evidence_json=None,
            gate_sha=gate_sha,
            reviewed_note_sha="missing-blob",
            reviewed_note_commit=None,
            reviewed_at="2026-04-04T08:35:54+02:00",
            review_kind="full-review",
        )
        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/sample.md",
            gate_id="prose/source-residue",
            model_id=TEST_MODEL,
            accepted_review_id=review_id,
            accepted_note_sha="missing-blob",
            accepted_note_commit=None,
            accepted_gate_sha=gate_sha,
            accepted_at="2026-04-04T08:36:13+02:00",
            acceptance_kind="full-review",
        )
        conn.commit()

    note.write_text(
        """---
description: Test note
type: note
traits: [title-as-claim]
tags: []
status: current
---
# Test note
Body.
""",
        encoding="utf-8",
    )
    commit_all(repo, "recover previous text fixture")

    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "commonplace.review.ack_trivial_note_changes",
            "--model",
            TEST_MODEL,
            "prose",
        ],
        cwd=repo,
        env=env,
        capture_output=True,
        text=True,
        check=True,
    )

    assert "acked: kb/notes/sample.md prose/source-residue" in result.stdout
