from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.lib import library
from commonplace.lib.review_workflows import results

GATE_ID = "prose/source-residue"
GATE_PATH = "kb/instructions/review-gates/prose/source-residue.md"


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def make_reviewable_note(path: Path, title: str = "Old note") -> Path:
    return write(
        path,
        f"""---
description: Test note
type: types/note.md
traits: []
---

# {title}

Body.
""",
    )


def make_gate(repo_root: Path) -> Path:
    return write(
        repo_root / GATE_PATH,
        """---
gate_id: prose/source-residue
name: Source Residue
lens: prose
watches: [body]
staleness: changed
---

## Failure mode

Fixture gate.
""",
    )


def seed_result(repo_root: Path, *, note_path: str) -> Path:
    """Write a review result for the note against the fixture gate; return its file."""
    result = results.make_result(
        note_path, (repo_root / note_path).read_text(encoding="utf-8"),
        GATE_PATH, (repo_root / GATE_PATH).read_text(encoding="utf-8"),
        outcome="pass", profile={"harness": "fake", "launch-model": "m", "effort": "low"}, model="m",
        run="run", launch="launch", completed_at="2026-04-10T08:05:00Z", body="## Result: PASS\n")
    return results.write_result(repo_root, result)


def use_repository_library(repo_root: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Make the repository's kb/ the library, as in a Commonplace checkout."""
    monkeypatch.setattr(library, "_library_root", lambda _override: (repo_root / "kb").resolve())
