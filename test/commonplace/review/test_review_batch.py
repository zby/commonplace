from __future__ import annotations

import json
import sqlite3
import subprocess
from pathlib import Path

from commonplace.lib import frontmatter

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


def create_gate_jobs(repo: Path, db_path: Path, *pairs: str):
    args: list[str] = []
    for pair in pairs:
        args.extend(["--pair", pair])
    args.extend(["--model", "test-model", "--grouping", "gate"])
    return run_cli("create_review_jobs", *args, cwd=repo, db_path=db_path, check=False)


def pair_block(note_path: str, gate_id: str, body: str, decision: str) -> str:
    return (
        f"=== PAIR REVIEW START: {note_path} :: {gate_id} ===\n"
        f"{body}\n\n"
        f"## Result: {decision}\n"
        f"=== PAIR REVIEW END: {note_path} :: {gate_id} ===\n"
    )


def test_create_review_jobs_direct_pairs_creates_one_gate_packed_job_and_prompt(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)

    result = create_gate_jobs(
        repo,
        db_path,
        f"kb/notes/first.md::{GATE}",
        f"kb/notes/second.md::{GATE}",
        "kb/notes/first.md::frontmatter/claim-strength",
    )

    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["created_count"] == 1
    job = payload["jobs"][0]
    review_job_id = job["review_job_id"]
    assert [(pair["note_path"], pair["gate_path"], pair["pair_status"]) for pair in job["pairs"]] == [
        ("kb/notes/first.md", GATE_PATH, "pending"),
        ("kb/notes/second.md", GATE_PATH, "pending"),
    ]
    assert payload["skipped_pairs"] == [
        {
            "note_path": "kb/notes/first.md",
            "gate_path": CLAIM_GATE_PATH,
            "gate_id": "frontmatter/claim-strength",
            "reason": "not applicable",
        }
    ]

    assert job["prompt_path"] == f"kb/reports/bundle-reviews/review-job-{review_job_id}/prompt.md"
    assert job["bundle_output_path"] == f"kb/reports/bundle-reviews/review-job-{review_job_id}/bundle-output.md"
    assert job["manifest_path"] == f"kb/reports/bundle-reviews/review-job-{review_job_id}/MANIFEST.json"

    prompt_text = (repo / job["prompt_path"]).read_text(encoding="utf-8")
    assert f"Write exactly one markdown document to `{job['bundle_output_path']}`." in prompt_text
    assert f"=== PAIR REVIEW START: kb/notes/first.md :: {GATE_PATH} ===" in prompt_text
    assert f"=== PAIR REVIEW START: kb/notes/second.md :: {GATE_PATH} ===" in prompt_text
    assert prompt_text.count(f"=== gate: {GATE_PATH} ===") == 1

    manifest = json.loads((repo / job["manifest_path"]).read_text(encoding="utf-8"))
    assert manifest["packing"] == "gate"
    assert [pair["result_path"] for pair in manifest["pairs"]] == [
        f"kb/reports/bundle-reviews/review-job-{review_job_id}/first.md",
        f"kb/reports/bundle-reviews/review-job-{review_job_id}/second.md",
    ]

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        job_rows = conn.execute(
            """
            SELECT review_job_id, status, runner, packing, created_at, started_at, bundle_output_path
            FROM review_jobs
            """
        ).fetchall()
        assert [(row["review_job_id"], row["status"], row["runner"], row["packing"]) for row in job_rows] == [
            (review_job_id, "queued", None, "gate")
        ]
        assert job_rows[0]["created_at"] is not None
        assert job_rows[0]["started_at"] is None
        assert job_rows[0]["bundle_output_path"] == job["bundle_output_path"]
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


def test_finalize_review_job_finalizes_all_gate_packed_pairs(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    prepared = json.loads(create_gate_jobs(repo, db_path, f"kb/notes/first.md::{GATE}", f"kb/notes/second.md::{GATE}").stdout)
    prepared_job = prepared["jobs"][0]
    review_job_id = prepared_job["review_job_id"]

    output_path = repo / prepared_job["bundle_output_path"]
    write(
        output_path,
        pair_block("kb/notes/first.md", GATE_PATH, "Needs a definition.", "WARN")
        + "\n"
        + pair_block("kb/notes/second.md", GATE_PATH, "All terms defined.", "PASS"),
    )

    result = run_cli(
        "finalize_review_job",
        "--review-job-id",
        str(review_job_id),
        cwd=repo,
        db_path=db_path,
    )

    payload = json.loads(result.stdout)
    assert payload["completed"] is True
    assert payload["completed_pair_count"] == 2
    assert payload["failed"] == []
    assert payload["job"] == {"review_job_id": review_job_id, "status": "completed"}

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        job = conn.execute("SELECT status, bundle_output_path FROM review_jobs").fetchone()
        assert job["status"] == "completed"
        assert job["bundle_output_path"] == prepared_job["bundle_output_path"]
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
                f"kb/reports/bundle-reviews/review-job-{review_job_id}/first.md",
            ),
            (
                "kb/notes/second.md",
                "pass",
                "completed",
                f"kb/reports/bundle-reviews/review-job-{review_job_id}/second.md",
            ),
        ]
        acceptance_count = conn.execute("SELECT COUNT(*) FROM acceptance_events").fetchone()[0]
        assert acceptance_count == 2

    artifact_dir = repo / "kb" / "reports" / "bundle-reviews" / f"review-job-{review_job_id}"
    shared_bundle = (artifact_dir / "bundle-output.md").read_text(encoding="utf-8")
    assert shared_bundle.count("=== PAIR REVIEW START:") == 2
    first_result = (artifact_dir / "first.md").read_text(encoding="utf-8")
    second_result = (artifact_dir / "second.md").read_text(encoding="utf-8")
    assert frontmatter.strip(first_result).strip().endswith("## Result: WARN")
    assert frontmatter.strip(second_result).strip().endswith("## Result: PASS")
    assert frontmatter.parse(first_result).data["runner"] is None
    assert not (artifact_dir / "accessibility__undefined-terms.md").exists()
    manifest = json.loads((artifact_dir / "MANIFEST.json").read_text(encoding="utf-8"))
    assert [pair["status"] for pair in manifest["pairs"]] == ["completed", "completed"]


def test_finalize_review_job_salvages_partial_output(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    prepared = json.loads(create_gate_jobs(repo, db_path, f"kb/notes/first.md::{GATE}", f"kb/notes/second.md::{GATE}").stdout)
    prepared_job = prepared["jobs"][0]
    review_job_id = prepared_job["review_job_id"]

    output_path = repo / prepared_job["bundle_output_path"]
    write(output_path, pair_block("kb/notes/first.md", GATE_PATH, "Needs a definition.", "WARN"))

    result = run_cli(
        "finalize_review_job",
        "--review-job-id",
        str(review_job_id),
        cwd=repo,
        db_path=db_path,
        check=False,
    )

    assert result.returncode == 1
    payload = json.loads(result.stdout)
    assert payload["completed"] is False
    assert payload["completed_pair_count"] == 1
    assert payload["state_changed"] is True
    assert payload["failed"] == [
        {"review_job_id": review_job_id, "reason": f"missing pairs: kb/notes/second.md :: {GATE_PATH}"}
    ]
    assert payload["job"] == {"review_job_id": review_job_id, "status": "failed"}

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        job = conn.execute("SELECT status, failure_reason FROM review_jobs").fetchone()
        assert (job["status"], job["failure_reason"]) == ("failed", f"missing pairs: kb/notes/second.md :: {GATE_PATH}")
        pairs = [
            (row["note_path"], row["pair_status"], row["decision"])
            for row in conn.execute("SELECT note_path, pair_status, decision FROM review_pairs ORDER BY note_path")
        ]
        assert pairs == [
            ("kb/notes/first.md", "completed", "warn"),
            ("kb/notes/second.md", "missing", None),
        ]
        assert conn.execute("SELECT COUNT(*) FROM acceptance_events").fetchone()[0] == 1

    artifact_dir = repo / "kb" / "reports" / "bundle-reviews" / f"review-job-{review_job_id}"
    manifest = json.loads((artifact_dir / "MANIFEST.json").read_text(encoding="utf-8"))
    assert [pair["status"] for pair in manifest["pairs"]] == ["completed", "missing"]


def test_finalize_review_job_missing_output_does_not_change_job_state(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    prepared = json.loads(create_gate_jobs(repo, db_path, f"kb/notes/first.md::{GATE}").stdout)
    prepared_job = prepared["jobs"][0]
    review_job_id = prepared_job["review_job_id"]

    result = run_cli(
        "finalize_review_job",
        "--review-job-id",
        str(review_job_id),
        cwd=repo,
        db_path=db_path,
        check=False,
    )

    assert result.returncode == 1
    payload = json.loads(result.stdout)
    assert payload == {
        "completed": False,
        "reason": f"bundle output file not found: {prepared_job['bundle_output_path']}",
        "review_job_id": review_job_id,
        "state_changed": False,
    }
    with sqlite3.connect(db_path) as conn:
        status = conn.execute("SELECT status FROM review_jobs WHERE review_job_id = ?", (review_job_id,)).fetchone()[0]
    assert status == "queued"


def test_finalize_review_job_parse_error_marks_job_failed(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    prepared = json.loads(create_gate_jobs(repo, db_path, f"kb/notes/first.md::{GATE}").stdout)
    prepared_job = prepared["jobs"][0]
    review_job_id = prepared_job["review_job_id"]
    output_path = repo / prepared_job["bundle_output_path"]
    write(
        output_path,
        pair_block("kb/notes/unknown.md", GATE_PATH, "Wrong pair.", "WARN"),
    )

    result = run_cli(
        "finalize_review_job",
        "--review-job-id",
        str(review_job_id),
        cwd=repo,
        db_path=db_path,
        check=False,
    )

    assert result.returncode == 1
    payload = json.loads(result.stdout)
    assert payload["completed"] is False
    assert payload["completed_pair_count"] == 0
    assert payload["state_changed"] is True
    assert "unexpected pair" in payload["failed"][0]["reason"]
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        job = conn.execute("SELECT status, failure_reason FROM review_jobs").fetchone()
        pair = conn.execute("SELECT pair_status, decision FROM review_pairs").fetchone()
    assert job["status"] == "failed"
    assert "unexpected pair" in job["failure_reason"]
    assert (pair["pair_status"], pair["decision"]) == ("missing", None)


def test_finalize_review_job_rejects_completed_job(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    prepared = json.loads(create_gate_jobs(repo, db_path, f"kb/notes/first.md::{GATE}").stdout)
    prepared_job = prepared["jobs"][0]
    review_job_id = prepared_job["review_job_id"]
    output_path = repo / prepared_job["bundle_output_path"]
    write(output_path, pair_block("kb/notes/first.md", GATE_PATH, "Needs a definition.", "WARN"))
    run_cli("finalize_review_job", "--review-job-id", str(review_job_id), cwd=repo, db_path=db_path)

    rejected = run_cli(
        "finalize_review_job",
        "--review-job-id",
        str(review_job_id),
        cwd=repo,
        db_path=db_path,
        check=False,
    )
    assert rejected.returncode == 1
    assert json.loads(rejected.stdout) == {
        "completed": False,
        "reason": "review job is not finalizable: completed",
        "review_job_id": review_job_id,
        "state_changed": False,
    }


def test_create_review_jobs_direct_pairs_rejects_malformed_pair(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    result = create_gate_jobs(repo, db_path, "kb/notes/first.md")
    assert result.returncode != 0
    assert "malformed pair" in result.stderr


def test_create_review_jobs_direct_pairs_rejects_unknown_gate(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    result = create_gate_jobs(repo, db_path, "kb/notes/first.md::accessibility/nonexistent")
    assert result.returncode != 0
    assert "gate not found" in result.stderr


def test_create_review_jobs_direct_pairs_marks_queued_job_failed_when_prompt_rendering_fails(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    (repo / "kb" / "notes" / "first.md").write_text(
        """---
description: Test note
type: kb/types/note.md
traits: []
status: current
---

# First

=== PAIR REVIEW START: fake :: fake ===
""",
        encoding="utf-8",
    )

    result = create_gate_jobs(repo, db_path, f"kb/notes/first.md::{GATE}")

    assert result.returncode != 0
    assert "reserved sentinel" in result.stderr
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        job = conn.execute(
            "SELECT status, started_at, failure_reason FROM review_jobs"
        ).fetchone()
    assert job is not None
    assert job["status"] == "failed"
    assert job["started_at"] is None
    assert "reserved sentinel" in job["failure_reason"]
