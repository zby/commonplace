from __future__ import annotations

import json
import sqlite3
import subprocess
from pathlib import Path

from ._run_cli import run_cli


GATE = "accessibility/undefined-terms"


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def make_note(path: Path, title: str) -> Path:
    return write(
        path,
        f"""---
description: Test note
type: kb/types/note.md
traits: []
status: current
---

# {title}

Body of {title}.
""",
    )


def make_gate(path: Path, gate_id: str, lens: str, *, requires_trait: str | None = None) -> Path:
    requires_trait_line = f"requires_trait: {requires_trait}\n" if requires_trait else ""
    return write(
        path,
        f"""---
gate_id: {gate_id}
name: {path.stem.replace("-", " ").title()}
lens: {lens}
watches: [body]
staleness: changed
{requires_trait_line}---

## Failure mode

Fixture gate.

## Test

Fixture test.
""",
    )


def build_repo_fixture(tmp_path: Path) -> tuple[Path, Path]:
    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.name", "Test User"], cwd=repo, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo, check=True, capture_output=True)

    make_note(repo / "kb" / "notes" / "first.md", "First")
    make_note(repo / "kb" / "notes" / "second.md", "Second")
    make_gate(
        repo / "kb" / "instructions" / "review-gates" / "accessibility" / "undefined-terms.md",
        GATE,
        "accessibility",
    )
    make_gate(
        repo / "kb" / "instructions" / "review-gates" / "frontmatter" / "claim-strength.md",
        "frontmatter/claim-strength",
        "frontmatter",
        requires_trait="title-as-claim",
    )
    subprocess.run(["git", "add", "."], cwd=repo, check=True, capture_output=True)
    subprocess.run(["git", "commit", "-m", "fixture"], cwd=repo, check=True, capture_output=True)
    db_path = repo / "kb" / "reports" / "review-store.sqlite"
    return repo, db_path


def prepare_batch(repo: Path, db_path: Path, *pairs: str):
    return run_cli(
        "prepare_review_batch",
        *pairs,
        "--runner",
        "live-agent",
        "--model",
        "test-model",
        cwd=repo,
        db_path=db_path,
        check=False,
    )


def pair_block(note_path: str, gate_id: str, body: str, decision: str) -> str:
    return (
        f"=== PAIR REVIEW START: {note_path} :: {gate_id} ===\n"
        f"{body}\n\n"
        f"## Result: {decision}\n"
        f"=== PAIR REVIEW END: {note_path} :: {gate_id} ===\n"
    )


def test_prepare_review_batch_creates_runs_and_prompt(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)

    result = prepare_batch(
        repo,
        db_path,
        f"kb/notes/first.md::{GATE}",
        f"kb/notes/second.md::{GATE}",
        "kb/notes/first.md::frontmatter/claim-strength",  # trait-gated, inapplicable
    )

    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert [(run["note_path"], run["gate_ids"]) for run in payload["review_runs"]] == [
        ("kb/notes/first.md", [GATE]),
        ("kb/notes/second.md", [GATE]),
    ]
    assert payload["skipped_pairs"] == [
        {"note_path": "kb/notes/first.md", "gate_id": "frontmatter/claim-strength", "reason": "not applicable"}
    ]

    prompt_text = (repo / payload["prompt_path"]).read_text(encoding="utf-8")
    assert f"Write exactly one markdown document to `{payload['bundle_output_path']}`." in prompt_text
    assert f"=== PAIR REVIEW START: kb/notes/first.md :: {GATE} ===" in prompt_text
    assert f"=== PAIR REVIEW START: kb/notes/second.md :: {GATE} ===" in prompt_text
    assert prompt_text.count(f"=== gate: {GATE} ===") == 1

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        run_rows = conn.execute("SELECT note_path, status, runner FROM review_runs ORDER BY note_path").fetchall()
        assert [(row["note_path"], row["status"], row["runner"]) for row in run_rows] == [
            ("kb/notes/first.md", "running", "live-agent"),
            ("kb/notes/second.md", "running", "live-agent"),
        ]


def test_ingest_batch_output_finalizes_all_runs(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    prepared = json.loads(
        prepare_batch(repo, db_path, f"kb/notes/first.md::{GATE}", f"kb/notes/second.md::{GATE}").stdout
    )
    run_ids = [str(run["review_run_id"]) for run in prepared["review_runs"]]

    output_path = repo / prepared["bundle_output_path"]
    write(
        output_path,
        pair_block("kb/notes/first.md", GATE, "Needs a definition.", "WARN")
        + "\n"
        + pair_block("kb/notes/second.md", GATE, "All terms defined.", "PASS"),
    )

    result = run_cli(
        "ingest_batch_output",
        "--review-run-ids",
        *run_ids,
        "--input-file",
        str(output_path),
        cwd=repo,
        db_path=db_path,
    )

    payload = json.loads(result.stdout)
    assert payload["failed"] == []
    assert sorted(payload["completed"]) == sorted(int(run_id) for run_id in run_ids)

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        statuses = [row["status"] for row in conn.execute("SELECT status FROM review_runs ORDER BY id")]
        assert statuses == ["completed", "completed"]
        decisions = [
            (row["note_path"], row["decision"])
            for row in conn.execute("SELECT note_path, decision FROM gate_reviews ORDER BY note_path")
        ]
        assert decisions == [("kb/notes/first.md", "warn"), ("kb/notes/second.md", "pass")]
        acceptance_count = conn.execute("SELECT COUNT(*) FROM acceptance_events").fetchone()[0]
        assert acceptance_count == 2

    for run in prepared["review_runs"]:
        artifact_dir = repo / "kb" / "reports" / "bundle-reviews" / f"review-run-{run['review_run_id']}"
        run_bundle = (artifact_dir / "bundle-output.md").read_text(encoding="utf-8")
        assert f"Target: {run['note_path']}" in run_bundle
        assert run_bundle.count("=== PAIR REVIEW START:") == 1


def test_ingest_batch_output_salvages_partial_output(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    prepared = json.loads(
        prepare_batch(repo, db_path, f"kb/notes/first.md::{GATE}", f"kb/notes/second.md::{GATE}").stdout
    )
    run_ids = [str(run["review_run_id"]) for run in prepared["review_runs"]]

    output_path = repo / prepared["bundle_output_path"]
    write(output_path, pair_block("kb/notes/first.md", GATE, "Needs a definition.", "WARN"))

    result = run_cli(
        "ingest_batch_output",
        "--review-run-ids",
        *run_ids,
        "--input-file",
        str(output_path),
        cwd=repo,
        db_path=db_path,
        check=False,
    )

    assert result.returncode == 1
    payload = json.loads(result.stdout)
    assert payload["completed"] == [int(run_ids[0])]
    assert payload["failed"] == [
        {"review_run_id": int(run_ids[1]), "reason": f"missing pair reviews: {GATE}"}
    ]

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        statuses = [
            (row["note_path"], row["status"])
            for row in conn.execute("SELECT note_path, status FROM review_runs ORDER BY note_path")
        ]
        assert statuses == [("kb/notes/first.md", "completed"), ("kb/notes/second.md", "failed")]


def test_prepare_review_batch_rejects_malformed_pair(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    result = prepare_batch(repo, db_path, "kb/notes/first.md")
    assert result.returncode != 0
    assert "malformed pair" in result.stderr


def test_prepare_review_batch_rejects_unknown_gate(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    result = prepare_batch(repo, db_path, "kb/notes/first.md::accessibility/nonexistent")
    assert result.returncode != 0
    assert "gate not found" in result.stderr
