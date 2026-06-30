from __future__ import annotations

import sqlite3
import subprocess
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.review import review_db
from commonplace.review import run_review_jobs as run_review_jobs_lib
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


def seed_accepted_review(
    repo: Path,
    db_path: Path,
    *,
    note_path: str,
    gate_path: str,
    model_partition: str,
) -> None:
    review_db.ensure_db(db_path)
    with review_db.connect(db_path) as conn:
        note_snapshot = review_db.snapshot_file(conn, repo_root=repo, path=note_path)
        gate_snapshot = review_db.snapshot_file(conn, repo_root=repo, path=gate_path)
        review_job_id = review_db.create_job_with_pairs(
            conn,
            model_partition=model_partition,
            runner="seed-runner",
            created_at="2026-04-10T10:00:00+00:00",
            started_at="2026-04-10T10:00:00+00:00",
            status="running",
            packing="gate",
            pairs=[
                review_db.ReviewPairRequest(
                    note_path=note_path,
                    gate_path=gate_path,
                    pair_ordinal=1,
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
                    reviewed_at="2026-04-10T10:01:00+00:00",
                )
            ],
            reviewed_at="2026-04-10T10:01:00+00:00",
        )
        review_pair = review_db.load_review_pairs_for_job(conn, review_job_id=review_job_id)[0]
        review_db.append_acceptance_event(
            conn,
            note_path=note_path,
            gate_path=gate_path,
            model_partition=model_partition,
            accepted_review_pair_id=review_pair.review_pair_id,
            accepted_note_snapshot_id=note_snapshot.snapshot_id,
            accepted_gate_snapshot_id=gate_snapshot.snapshot_id,
            accepted_at="2026-04-10T10:02:00+00:00",
        )
        conn.commit()


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
    monkeypatch.setattr(run_review_jobs_lib, "run_prompt", _fake_run_prompt_factory(bundle_output))

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
        job_rows = conn.execute(
            "SELECT review_job_id, status, packing, bundle_output_path FROM review_jobs"
        ).fetchall()
        assert [(row["status"], row["packing"]) for row in job_rows] == [("completed", "gate")]

        pair_rows = conn.execute(
            "SELECT note_path, decision, result_path, pair_status FROM review_pairs ORDER BY note_path"
        ).fetchall()
        assert [(row["note_path"], row["decision"], row["pair_status"]) for row in pair_rows] == [
            ("kb/notes/first.md", "warn", "completed"),
            ("kb/notes/second.md", "pass", "completed"),
        ]

        acceptance_count = conn.execute("SELECT COUNT(*) FROM acceptance_events").fetchone()[0]
        assert acceptance_count == 2

    artifact_dir = repo / "kb" / "reports" / "bundle-reviews" / f"review-job-{job_rows[0]['review_job_id']}"
    assert job_rows[0]["bundle_output_path"] == f"kb/reports/bundle-reviews/review-job-{job_rows[0]['review_job_id']}/bundle-output.md"
    assert (artifact_dir / "bundle-output.md").read_text(encoding="utf-8").count("=== PAIR REVIEW START:") == 2
    assert frontmatter.strip((repo / pair_rows[0]["result_path"]).read_text(encoding="utf-8")) == (
        "Needs a definition for Alpha.\n\n## Result: WARN\n"
    )
    assert frontmatter.strip((repo / pair_rows[1]["result_path"]).read_text(encoding="utf-8")) == (
        "No undefined terms found.\n\n## Result: PASS\n"
    )


def test_run_gate_sweep_can_select_pairs_missing_any_review(monkeypatch, tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    seed_accepted_review(
        repo,
        db_path,
        note_path="kb/notes/first.md",
        gate_path=GATE_PATH,
        model_partition="other-model",
    )

    bundle_output = (
        f"=== PAIR REVIEW START: kb/notes/second.md :: {GATE_PATH} ===\n"
        "No undefined terms found.\n\n"
        "## Result: PASS\n"
        f"=== PAIR REVIEW END: kb/notes/second.md :: {GATE_PATH} ===\n"
    )
    monkeypatch.setattr(run_review_jobs_lib, "run_prompt", _fake_run_prompt_factory(bundle_output))

    result = run_gate_sweep(
        repo,
        "accessibility/undefined-terms",
        "--runner",
        "codex",
        "--model",
        "test-model",
        "--missing-any-review",
        "--batch-size",
        "2",
        "--note",
        "kb/notes/first.md",
        "kb/notes/second.md",
        "--db",
        str(db_path),
    )

    assert result.returncode == 0
    assert "Batch 1/1: launching codex for 1 notes" in result.stderr
    assert "kb/notes/first.md" not in result.stderr
    assert "kb/notes/second.md" in result.stderr
    assert "Reviewed: 1 notes" in result.stdout

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        new_pair_rows = conn.execute(
            """
            SELECT rp.note_path, j.model_partition, rp.pair_status, rp.decision
            FROM review_pairs AS rp
            JOIN review_jobs AS j ON rp.review_job_id = j.review_job_id
            WHERE j.model_partition = 'test-model'
            ORDER BY rp.note_path
            """
        ).fetchall()
        assert [(row["note_path"], row["pair_status"], row["decision"]) for row in new_pair_rows] == [
            ("kb/notes/second.md", "completed", "pass")
        ]


def test_run_gate_sweep_salvages_parsed_notes_and_fails_missing_ones(monkeypatch, tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)

    # Output covers only the first note; the second note's pair is missing.
    bundle_output = (
        f"=== PAIR REVIEW START: kb/notes/first.md :: {GATE_PATH} ===\n"
        "Needs a definition for Alpha.\n\n"
        "## Result: WARN\n"
        f"=== PAIR REVIEW END: kb/notes/first.md :: {GATE_PATH} ===\n"
    )
    monkeypatch.setattr(run_review_jobs_lib, "run_prompt", _fake_run_prompt_factory(bundle_output))

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
    assert "Failed:   1 job(s)" in result.stderr

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        job_row = conn.execute(
            "SELECT review_job_id, status, failure_reason, bundle_output_path FROM review_jobs"
        ).fetchone()
        assert job_row["status"] == "failed"
        assert f"missing pairs: kb/notes/second.md :: {GATE_PATH}" in job_row["failure_reason"]

        pair_rows = conn.execute(
            "SELECT note_path, pair_status, decision, result_path FROM review_pairs ORDER BY note_path"
        ).fetchall()
        assert [(row["note_path"], row["pair_status"], row["decision"]) for row in pair_rows] == [
            ("kb/notes/first.md", "completed", "warn"),
            ("kb/notes/second.md", "missing", None),
        ]
        acceptance_count = conn.execute("SELECT COUNT(*) FROM acceptance_events").fetchone()[0]
        assert acceptance_count == 1

    artifact_dir = repo / "kb" / "reports" / "bundle-reviews" / f"review-job-{job_row['review_job_id']}"
    assert f"kb/notes/first.md :: {GATE_PATH}" in (repo / job_row["bundle_output_path"]).read_text(encoding="utf-8")
    assert frontmatter.strip((repo / pair_rows[0]["result_path"]).read_text(encoding="utf-8")) == (
        "Needs a definition for Alpha.\n\n## Result: WARN\n"
    )
    assert not (artifact_dir / "second.md").exists()
