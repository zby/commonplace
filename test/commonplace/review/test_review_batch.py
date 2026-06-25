from __future__ import annotations

import json
import sqlite3
import subprocess
from pathlib import Path

from ._run_cli import run_cli


GATE = "accessibility/undefined-terms"
GATE_PATH = "kb/instructions/review-gates/accessibility/undefined-terms.md"
CLAIM_GATE_PATH = "kb/instructions/review-gates/frontmatter/claim-strength.md"


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


def test_prepare_review_batch_creates_one_gate_packed_run_and_prompt(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)

    result = prepare_batch(
        repo,
        db_path,
        f"kb/notes/first.md::{GATE}",
        f"kb/notes/second.md::{GATE}",
        "kb/notes/first.md::frontmatter/claim-strength",
    )

    assert result.returncode == 0
    payload = json.loads(result.stdout)
    review_run_id = payload["review_run_id"]
    assert [(pair["note_path"], pair["gate_path"], pair["status"]) for pair in payload["pairs"]] == [
        ("kb/notes/first.md", GATE_PATH, "pending"),
        ("kb/notes/second.md", GATE_PATH, "pending"),
    ]
    assert payload["skipped_pairs"] == [
        {"note_path": "kb/notes/first.md", "gate_path": CLAIM_GATE_PATH, "reason": "not applicable"}
    ]

    assert payload["prompt_path"] == f"kb/reports/bundle-reviews/review-run-{review_run_id}/prompt.md"
    assert payload["bundle_output_path"] == f"kb/reports/bundle-reviews/review-run-{review_run_id}/bundle-output.md"
    assert payload["manifest_path"] == f"kb/reports/bundle-reviews/review-run-{review_run_id}/MANIFEST.json"

    prompt_text = (repo / payload["prompt_path"]).read_text(encoding="utf-8")
    assert f"Write exactly one markdown document to `{payload['bundle_output_path']}`." in prompt_text
    assert f"=== PAIR REVIEW START: kb/notes/first.md :: {GATE_PATH} ===" in prompt_text
    assert f"=== PAIR REVIEW START: kb/notes/second.md :: {GATE_PATH} ===" in prompt_text
    assert prompt_text.count(f"=== gate: {GATE_PATH} ===") == 1

    manifest = json.loads((repo / payload["manifest_path"]).read_text(encoding="utf-8"))
    assert manifest["packing"] == "gate"
    assert [pair["result_path"] for pair in manifest["pairs"]] == [
        f"kb/reports/bundle-reviews/review-run-{review_run_id}/first.md",
        f"kb/reports/bundle-reviews/review-run-{review_run_id}/second.md",
    ]

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        run_rows = conn.execute(
            "SELECT review_run_id, status, runner, packing, bundle_output_path FROM review_runs"
        ).fetchall()
        assert [(row["review_run_id"], row["status"], row["runner"], row["packing"]) for row in run_rows] == [
            (review_run_id, "running", "live-agent", "gate")
        ]
        assert run_rows[0]["bundle_output_path"] == payload["bundle_output_path"]
        pair_rows = conn.execute(
            """
            SELECT
                note_path,
                gate_path,
                pair_status,
                result_path,
                reviewed_note_snapshot_id,
                reviewed_gate_snapshot_id
            FROM review_pairs
            ORDER BY pair_ordinal
            """
        ).fetchall()
        assert [(row["note_path"], row["gate_path"], row["pair_status"]) for row in pair_rows] == [
            ("kb/notes/first.md", GATE_PATH, "pending"),
            ("kb/notes/second.md", GATE_PATH, "pending"),
        ]
        assert [row["result_path"] for row in pair_rows] == [pair["result_path"] for pair in manifest["pairs"]]
        assert all(row["reviewed_note_snapshot_id"] is not None for row in pair_rows)
        assert all(row["reviewed_gate_snapshot_id"] is not None for row in pair_rows)


def test_ingest_batch_output_finalizes_all_pairs(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    prepared = json.loads(
        prepare_batch(repo, db_path, f"kb/notes/first.md::{GATE}", f"kb/notes/second.md::{GATE}").stdout
    )
    review_run_id = prepared["review_run_id"]

    output_path = repo / prepared["bundle_output_path"]
    write(
        output_path,
        pair_block("kb/notes/first.md", GATE_PATH, "Needs a definition.", "WARN")
        + "\n"
        + pair_block("kb/notes/second.md", GATE_PATH, "All terms defined.", "PASS"),
    )

    result = run_cli(
        "ingest_batch_output",
        "--review-run-id",
        str(review_run_id),
        "--input-file",
        str(output_path),
        cwd=repo,
        db_path=db_path,
    )

    payload = json.loads(result.stdout)
    assert payload["failed"] == []
    assert payload["completed"] == [review_run_id]

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        run = conn.execute("SELECT status, bundle_output_path FROM review_runs").fetchone()
        assert run["status"] == "completed"
        assert run["bundle_output_path"] == prepared["bundle_output_path"]
        decisions = [
            (row["note_path"], row["decision"], row["pair_status"], row["result_path"])
            for row in conn.execute(
                "SELECT note_path, decision, pair_status, result_path FROM review_pairs ORDER BY note_path"
            )
        ]
        assert decisions == [
            (
                "kb/notes/first.md",
                "warn",
                "completed",
                f"kb/reports/bundle-reviews/review-run-{review_run_id}/first.md",
            ),
            (
                "kb/notes/second.md",
                "pass",
                "completed",
                f"kb/reports/bundle-reviews/review-run-{review_run_id}/second.md",
            ),
        ]
        acceptance_count = conn.execute("SELECT COUNT(*) FROM acceptance_events").fetchone()[0]
        assert acceptance_count == 2

    artifact_dir = repo / "kb" / "reports" / "bundle-reviews" / f"review-run-{review_run_id}"
    shared_bundle = (artifact_dir / "bundle-output.md").read_text(encoding="utf-8")
    assert shared_bundle.count("=== PAIR REVIEW START:") == 2
    assert (artifact_dir / "first.md").read_text(encoding="utf-8").strip().endswith("## Result: WARN")
    assert (artifact_dir / "second.md").read_text(encoding="utf-8").strip().endswith("## Result: PASS")
    assert not (artifact_dir / "accessibility__undefined-terms.md").exists()
    manifest = json.loads((artifact_dir / "MANIFEST.json").read_text(encoding="utf-8"))
    assert [pair["status"] for pair in manifest["pairs"]] == ["completed", "completed"]


def test_ingest_batch_output_salvages_partial_output(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    prepared = json.loads(
        prepare_batch(repo, db_path, f"kb/notes/first.md::{GATE}", f"kb/notes/second.md::{GATE}").stdout
    )
    review_run_id = prepared["review_run_id"]

    output_path = repo / prepared["bundle_output_path"]
    write(output_path, pair_block("kb/notes/first.md", GATE_PATH, "Needs a definition.", "WARN"))

    result = run_cli(
        "ingest_batch_output",
        "--review-run-id",
        str(review_run_id),
        "--input-file",
        str(output_path),
        cwd=repo,
        db_path=db_path,
        check=False,
    )

    assert result.returncode == 1
    payload = json.loads(result.stdout)
    assert payload["completed"] == []
    assert payload["failed"] == [
        {"review_run_id": review_run_id, "reason": f"missing pairs: kb/notes/second.md :: {GATE_PATH}"}
    ]

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        run = conn.execute("SELECT status, failure_reason FROM review_runs").fetchone()
        assert (run["status"], run["failure_reason"]) == ("failed", f"missing pairs: kb/notes/second.md :: {GATE_PATH}")
        pairs = [
            (row["note_path"], row["pair_status"], row["decision"])
            for row in conn.execute("SELECT note_path, pair_status, decision FROM review_pairs ORDER BY note_path")
        ]
        assert pairs == [
            ("kb/notes/first.md", "completed", "warn"),
            ("kb/notes/second.md", "missing", None),
        ]
        assert conn.execute("SELECT COUNT(*) FROM acceptance_events").fetchone()[0] == 1

    artifact_dir = repo / "kb" / "reports" / "bundle-reviews" / f"review-run-{review_run_id}"
    manifest = json.loads((artifact_dir / "MANIFEST.json").read_text(encoding="utf-8"))
    assert [pair["status"] for pair in manifest["pairs"]] == ["completed", "missing"]


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
