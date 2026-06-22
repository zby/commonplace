from __future__ import annotations

import json
import sqlite3
import subprocess
from pathlib import Path

from commonplace.review import executor
from commonplace.review.runners import RunnerResult

from ._run_cli import run_cli


GATE_ONE = "accessibility/undefined-terms"
GATE_TWO = "prose/source-residue"


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
status: current
---

# Test note

Term Alpha appears before its definition.
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
    make_note(repo / "kb" / "notes" / "sample.md")
    make_gate(
        repo / "kb" / "instructions" / "review-gates" / "accessibility" / "undefined-terms.md",
        GATE_ONE,
        "accessibility",
    )
    make_gate(
        repo / "kb" / "instructions" / "review-gates" / "prose" / "source-residue.md",
        GATE_TWO,
        "prose",
    )
    commit_all(repo, "fixture")
    return repo, repo / "kb" / "reports" / "review-store.sqlite"


def pair_block(note_path: str, gate_id: str, body: str, decision: str) -> str:
    return (
        f"=== PAIR REVIEW START: {note_path} :: {gate_id} ===\n"
        f"{body}\n\n"
        f"## Result: {decision}\n"
        f"=== PAIR REVIEW END: {note_path} :: {gate_id} ===\n"
    )


def bundle_output() -> str:
    return (
        pair_block("kb/notes/sample.md", GATE_ONE, "Needs a definition for Alpha.", "WARN")
        + "\n"
        + pair_block("kb/notes/sample.md", GATE_TWO, "No residue found.", "PASS")
    )


def test_create_review_run_with_prompt_creates_one_note_packed_run(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)

    result = run_cli(
        "create_review_run",
        "kb/notes/sample.md",
        GATE_ONE,
        GATE_TWO,
        "--runner",
        "live-agent",
        "--model",
        "test-model",
        "--with-prompt",
        "--json",
        cwd=repo,
        db_path=db_path,
    )

    payload = json.loads(result.stdout)
    review_run_id = payload["review_run_id"]
    assert payload["gate_ids"] == [GATE_ONE, GATE_TWO]
    assert payload["prompt_path"] == f"kb/reports/bundle-reviews/review-run-{review_run_id}/prompt.md"
    assert payload["manifest_path"] == f"kb/reports/bundle-reviews/review-run-{review_run_id}/MANIFEST.json"

    prompt = (repo / payload["prompt_path"]).read_text(encoding="utf-8")
    assert f"=== PAIR REVIEW START: kb/notes/sample.md :: {GATE_ONE} ===" in prompt
    assert f"=== PAIR REVIEW START: kb/notes/sample.md :: {GATE_TWO} ===" in prompt
    manifest = json.loads((repo / payload["manifest_path"]).read_text(encoding="utf-8"))
    assert manifest["packing"] == "note"
    assert [pair["result_path"] for pair in manifest["pairs"]] == [
        f"kb/reports/bundle-reviews/review-run-{review_run_id}/accessibility__undefined-terms.md",
        f"kb/reports/bundle-reviews/review-run-{review_run_id}/prose__source-residue.md",
    ]

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        run = conn.execute("SELECT status, runner, packing FROM review_runs").fetchone()
        assert (run["status"], run["runner"], run["packing"]) == ("running", "live-agent", "note")
        pair_rows = conn.execute("SELECT gate_id, pair_status FROM review_pairs ORDER BY pair_ordinal").fetchall()
        assert [(row["gate_id"], row["pair_status"]) for row in pair_rows] == [
            (GATE_ONE, "pending"),
            (GATE_TWO, "pending"),
        ]
        run_columns = {row["name"] for row in conn.execute("PRAGMA table_info(review_runs)").fetchall()}
        assert "note_path" not in run_columns
        assert "reviewed_note_sha" not in run_columns


def test_ingest_bundle_output_finalizes_review_pairs(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    prepared = json.loads(
        run_cli(
            "create_review_run",
            "kb/notes/sample.md",
            GATE_ONE,
            GATE_TWO,
            "--runner",
            "live-agent",
            "--model",
            "test-model",
            "--with-prompt",
            "--json",
            cwd=repo,
            db_path=db_path,
        ).stdout
    )
    output_path = repo / prepared["bundle_output_path"]
    output_path.write_text(bundle_output(), encoding="utf-8")

    result = run_cli(
        "ingest_bundle_output",
        "--review-run-id",
        str(prepared["review_run_id"]),
        "--input-file",
        str(output_path),
        cwd=repo,
        db_path=db_path,
    )

    assert result.stdout.strip() == f"completed {prepared['review_run_id']} 2"
    artifact_dir = repo / "kb" / "reports" / "bundle-reviews" / f"review-run-{prepared['review_run_id']}"
    assert (artifact_dir / "accessibility__undefined-terms.md").read_text(encoding="utf-8").strip().endswith(
        "## Result: WARN"
    )
    assert (artifact_dir / "prose__source-residue.md").read_text(encoding="utf-8").strip().endswith("## Result: PASS")
    assert not (artifact_dir / "kb__notes__sample.md :: accessibility__undefined-terms.md").exists()
    manifest = json.loads((artifact_dir / "MANIFEST.json").read_text(encoding="utf-8"))
    assert [pair["status"] for pair in manifest["pairs"]] == ["completed", "completed"]
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        run = conn.execute("SELECT status FROM review_runs").fetchone()
        assert run["status"] == "completed"
        pairs = conn.execute("SELECT gate_id, decision, pair_status FROM review_pairs ORDER BY pair_ordinal").fetchall()
        assert [(row["gate_id"], row["decision"], row["pair_status"]) for row in pairs] == [
            (GATE_ONE, "warn", "completed"),
            (GATE_TWO, "pass", "completed"),
        ]
        assert conn.execute("SELECT COUNT(*) FROM acceptance_events").fetchone()[0] == 2


def test_run_review_bundle_with_fake_runner_completes_pairs(monkeypatch, tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)

    def fake_run_prompt(**_kwargs):
        return RunnerResult(stdout=bundle_output(), stderr="", returncode=0, telemetry=None)

    monkeypatch.setattr(executor, "run_prompt", fake_run_prompt)

    result = run_cli(
        "run_review_bundle",
        "kb/notes/sample.md",
        GATE_ONE,
        GATE_TWO,
        "--runner",
        "codex",
        "--model",
        "test-model",
        cwd=repo,
        db_path=db_path,
    )

    assert result.returncode == 0
    assert "completed 1 2" in result.stdout
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        run = conn.execute("SELECT status, packing FROM review_runs").fetchone()
        assert (run["status"], run["packing"]) == ("completed", "note")
        decisions = [row["decision"] for row in conn.execute("SELECT decision FROM review_pairs ORDER BY pair_ordinal")]
        assert decisions == ["warn", "pass"]


def test_run_review_bundle_parse_failure_persists_raw_bundle(monkeypatch, tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)

    def fake_run_prompt(**_kwargs):
        return RunnerResult(stdout="not a pair bundle\n", stderr="", returncode=0, telemetry=None)

    monkeypatch.setattr(executor, "run_prompt", fake_run_prompt)

    result = run_cli(
        "run_review_bundle",
        "kb/notes/sample.md",
        GATE_ONE,
        "--runner",
        "codex",
        "--model",
        "test-model",
        cwd=repo,
        db_path=db_path,
        check=False,
    )

    assert result.returncode == 1
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        run = conn.execute("SELECT status, raw_bundle_markdown, failure_reason FROM review_runs").fetchone()
        assert run["status"] == "failed"
        assert run["raw_bundle_markdown"] == "not a pair bundle\n"
        assert "missing" in run["failure_reason"] or "pair" in run["failure_reason"]
