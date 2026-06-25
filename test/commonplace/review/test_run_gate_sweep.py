from __future__ import annotations

import sqlite3
import subprocess
from pathlib import Path

from commonplace.review import executor
from commonplace.review.runners import RunnerResult

from ._run_cli import run_cli


REPO_ROOT = Path(__file__).resolve().parents[3]
GATE_PATH = "kb/instructions/review-gates/accessibility/undefined-terms.md"


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def make_note(path: Path, title: str, body: str) -> Path:
    return write(
        path,
        f"""---
description: Test note
type: kb/types/note.md
traits: []
status: current
---

# {title}
{body}
""",
    )


def make_gate(path: Path, gate_id: str, lens: str) -> Path:
    return write(
        path,
        f"""---
gate_id: {gate_id}
name: {path.stem.replace("-", " ").title()}
lens: {lens}
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


def commit_all(path: Path, message: str) -> None:
    subprocess.run(["git", "add", "."], cwd=path, check=True, capture_output=True)
    subprocess.run(["git", "commit", "-m", message], cwd=path, check=True, capture_output=True)


def build_repo_fixture(tmp_path: Path) -> tuple[Path, Path]:
    repo = tmp_path / "repo"
    repo.mkdir()
    init_repo(repo)

    make_note(repo / "kb" / "notes" / "first.md", "First", "\nTerm Alpha appears before its definition.\n")
    make_note(repo / "kb" / "notes" / "second.md", "Second", "\nAll terms are defined.\n")
    make_gate(
        repo / "kb" / "instructions" / "review-gates" / "accessibility" / "undefined-terms.md",
        "accessibility/undefined-terms",
        "accessibility",
    )
    commit_all(repo, "fixture")
    db_path = repo / "kb" / "reports" / "review-store.sqlite"
    return repo, db_path


def run_gate_sweep(repo: Path, *args: str):
    return run_cli("run_gate_sweep", *args, cwd=repo, check=False)


def _fake_run_prompt_factory(stdout: str, *, returncode: int = 0):
    def fake_run_prompt(**_kwargs):
        return RunnerResult(stdout=stdout, stderr="", returncode=returncode, telemetry=None)

    return fake_run_prompt


def test_run_gate_sweep_reviews_multiple_notes_in_one_batch(monkeypatch, tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)

    bundle_output = (
        f"=== PAIR REVIEW START: kb/notes/first.md :: {GATE_PATH} ===\n"
        "Needs a definition for Alpha.\n\n"
        "## Result: WARN\n"
        f"=== PAIR REVIEW END: kb/notes/first.md :: {GATE_PATH} ===\n\n"
        f"=== PAIR REVIEW START: kb/notes/second.md :: {GATE_PATH} ===\n"
        "No undefined terms found.\n\n"
        "## Result: PASS\n"
        f"=== PAIR REVIEW END: kb/notes/second.md :: {GATE_PATH} ===\n"
    )
    monkeypatch.setattr(executor, "run_prompt", _fake_run_prompt_factory(bundle_output))

    result = run_gate_sweep(
        repo,
        "accessibility/undefined-terms",
        "--runner",
        "codex",
        "--model",
        "test-model",
        "--batch-size",
        "2",
        "--note",
        "kb/notes/first.md",
        "kb/notes/second.md",
        "--db",
        str(db_path),
    )

    assert result.returncode == 0
    assert "Batch 1/1: reviewed 2 notes" in result.stdout
    assert "Reviewed: 2 notes" in result.stdout

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        run_rows = conn.execute(
            "SELECT review_run_id, status, packing, raw_bundle_markdown FROM review_runs"
        ).fetchall()
        assert [(row["status"], row["packing"]) for row in run_rows] == [("completed", "gate")]
        assert run_rows[0]["raw_bundle_markdown"].count("=== PAIR REVIEW START:") == 2

        pair_rows = conn.execute(
            "SELECT note_path, decision, rationale_markdown, pair_status FROM review_pairs ORDER BY note_path"
        ).fetchall()
        assert [(row["note_path"], row["decision"], row["pair_status"]) for row in pair_rows] == [
            ("kb/notes/first.md", "warn", "completed"),
            ("kb/notes/second.md", "pass", "completed"),
        ]
        assert pair_rows[0]["rationale_markdown"] == "Needs a definition for Alpha.\n\n## Result: WARN\n"
        assert pair_rows[1]["rationale_markdown"] == "No undefined terms found.\n\n## Result: PASS\n"

        acceptance_count = conn.execute("SELECT COUNT(*) FROM acceptance_events").fetchone()[0]
        assert acceptance_count == 2

    artifact_dir = repo / "kb" / "reports" / "bundle-reviews" / f"review-run-{run_rows[0]['review_run_id']}"
    assert (artifact_dir / "bundle-output.md").read_text(encoding="utf-8") == run_rows[0]["raw_bundle_markdown"]


def test_run_gate_sweep_salvages_parsed_notes_and_fails_missing_ones(monkeypatch, tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)

    # Output covers only the first note; the second note's pair is missing.
    bundle_output = (
        f"=== PAIR REVIEW START: kb/notes/first.md :: {GATE_PATH} ===\n"
        "Needs a definition for Alpha.\n\n"
        "## Result: WARN\n"
        f"=== PAIR REVIEW END: kb/notes/first.md :: {GATE_PATH} ===\n"
    )
    monkeypatch.setattr(executor, "run_prompt", _fake_run_prompt_factory(bundle_output))

    result = run_gate_sweep(
        repo,
        "accessibility/undefined-terms",
        "--runner",
        "codex",
        "--model",
        "test-model",
        "--batch-size",
        "2",
        "--note",
        "kb/notes/first.md",
        "kb/notes/second.md",
        "--db",
        str(db_path),
    )

    assert result.returncode == 1
    assert f"missing pairs: kb/notes/second.md :: {GATE_PATH}" in result.stderr
    assert "Batch 1/1: reviewed 1 notes" in result.stdout
    assert "Reviewed: 1 notes" in result.stdout
    assert "Missing:  1 notes" in result.stderr
    assert "Failed:   1 run(s)" in result.stderr

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        run_row = conn.execute(
            "SELECT status, failure_reason, raw_bundle_markdown FROM review_runs"
        ).fetchone()
        assert run_row["status"] == "failed"
        assert f"missing pairs: kb/notes/second.md :: {GATE_PATH}" in run_row["failure_reason"]
        assert f"kb/notes/first.md :: {GATE_PATH}" in run_row["raw_bundle_markdown"]

        pair_rows = conn.execute("SELECT note_path, pair_status, decision FROM review_pairs ORDER BY note_path").fetchall()
        assert [(row["note_path"], row["pair_status"], row["decision"]) for row in pair_rows] == [
            ("kb/notes/first.md", "completed", "warn"),
            ("kb/notes/second.md", "missing", None),
        ]
        acceptance_count = conn.execute("SELECT COUNT(*) FROM acceptance_events").fetchone()[0]
        assert acceptance_count == 1
