from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.review import run_review_jobs as run_review_jobs_lib
from commonplace.review.runners import RunnerResult

from ._run_cli import run_cli
from .test_review_jobs_live_and_direct import (
    GATE_ONE,
    build_repo_fixture,
    single_pair_bundle_output,
)


def _create_single_job(repo: Path, db_path: Path, *, model: str = "test-model") -> dict[str, object]:
    payload = json.loads(
        run_cli(
            "create_review_jobs",
            "--note",
            "kb/notes/sample.md",
            GATE_ONE,
            "--model",
            model,
            "--grouping",
            "note",
            cwd=repo,
            db_path=db_path,
        ).stdout
    )
    return payload["jobs"][0]


def test_run_review_jobs_executes_claims_and_finalizes_explicit_job(monkeypatch, tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    job = _create_single_job(repo, db_path)
    prompts: list[dict[str, object]] = []

    def fake_run_prompt(**kwargs):
        prompts.append(kwargs)
        return RunnerResult(
            stdout=single_pair_bundle_output(),
            stderr="diagnostic line\n",
            returncode=0,
            telemetry={"model": "test-model", "reasoning_effort": "high"},
        )

    monkeypatch.setattr(run_review_jobs_lib, "run_prompt", fake_run_prompt)

    result = run_cli(
        "run_review_jobs",
        "--runner",
        "codex",
        "--model",
        "test-model",
        "--review-job-id",
        str(job["review_job_id"]),
        cwd=repo,
        db_path=db_path,
    )

    payload = json.loads(result.stdout)
    assert payload["completed_count"] == 1
    assert payload["failed_count"] == 0
    assert payload["jobs"][0]["status"] == "completed"
    assert payload["jobs"][0]["runner_returncode"] == 0
    assert payload["jobs"][0]["bundle_output_path"] == job["bundle_output_path"]
    assert payload["jobs"][0]["debug_log_path"] == f"kb/reports/bundle-reviews/review-job-{job['review_job_id']}/debug.log"
    assert prompts[0]["model"] == "test-model"
    assert prompts[0]["effort"] is None
    assert prompts[0]["prompt"] == (repo / job["prompt_path"]).read_text(encoding="utf-8")
    assert (repo / job["bundle_output_path"]).read_text(encoding="utf-8") == single_pair_bundle_output()
    assert "diagnostic line" in (repo / payload["jobs"][0]["debug_log_path"]).read_text(encoding="utf-8")

    result_text = (repo / job["pairs"][0]["result_path"]).read_text(encoding="utf-8")
    parsed = frontmatter.parse(result_text)
    assert parsed.data["runner_model"] == "test-model"
    assert parsed.data["runner_effort"] == "high"
    assert frontmatter.strip(result_text) == "Needs a definition for Alpha.\n\n## Result: WARN\n"
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_job = conn.execute(
            "SELECT status, runner, runner_model, runner_effort, telemetry_json FROM review_jobs"
        ).fetchone()
    assert db_job["status"] == "completed"
    assert db_job["runner"] == "codex"
    assert db_job["runner_model"] == "test-model"
    assert db_job["runner_effort"] == "high"
    assert json.loads(db_job["telemetry_json"]) == {"model": "test-model", "reasoning_effort": "high"}


def test_run_review_jobs_queue_mode_respects_partition_and_limit(monkeypatch, tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    first = _create_single_job(repo, db_path)
    second = _create_single_job(repo, db_path)
    other = _create_single_job(repo, db_path, model="other-model")

    def fake_run_prompt(**_kwargs):
        return RunnerResult(stdout=single_pair_bundle_output(), stderr="", returncode=0, telemetry=None)

    monkeypatch.setattr(run_review_jobs_lib, "run_prompt", fake_run_prompt)

    result = run_cli(
        "run_review_jobs",
        "--runner",
        "codex",
        "--model",
        "test-model",
        "--limit",
        "1",
        cwd=repo,
        db_path=db_path,
    )

    payload = json.loads(result.stdout)
    assert payload["selected_count"] == 1
    assert payload["completed_count"] == 1
    assert payload["jobs"][0]["review_job_id"] == first["review_job_id"]
    with sqlite3.connect(db_path) as conn:
        rows = conn.execute(
            "SELECT review_job_id, status FROM review_jobs ORDER BY review_job_id"
        ).fetchall()
    assert rows == [
        (first["review_job_id"], "completed"),
        (second["review_job_id"], "queued"),
        (other["review_job_id"], "queued"),
    ]


def test_run_review_jobs_nonzero_runner_marks_pairs_missing(monkeypatch, tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    job = _create_single_job(repo, db_path)

    def fake_run_prompt(**_kwargs):
        return RunnerResult(stdout="partial diagnostic\n", stderr="failed\n", returncode=7, telemetry=None)

    monkeypatch.setattr(run_review_jobs_lib, "run_prompt", fake_run_prompt)

    result = run_cli(
        "run_review_jobs",
        "--runner",
        "codex",
        "--model",
        "test-model",
        "--review-job-id",
        str(job["review_job_id"]),
        cwd=repo,
        db_path=db_path,
        check=False,
    )

    payload = json.loads(result.stdout)
    assert result.returncode == 1
    assert payload["jobs"][0]["status"] == "failed"
    assert payload["jobs"][0]["failure_reason"] == "codex exited 7"
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        pair = conn.execute("SELECT pair_status, decision FROM review_pairs").fetchone()
    assert (pair["pair_status"], pair["decision"]) == ("missing", None)


def test_run_review_jobs_explicit_preflight_reports_distinct_failures(monkeypatch, tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    wrong_partition = _create_single_job(repo, db_path)
    missing_path = _create_single_job(repo, db_path)
    nonqueued = _create_single_job(repo, db_path)

    def fail_if_called(**_kwargs):
        raise AssertionError("runner should not be invoked")

    monkeypatch.setattr(run_review_jobs_lib, "run_prompt", fail_if_called)
    with sqlite3.connect(db_path) as conn:
        conn.execute("UPDATE review_jobs SET prompt_path = NULL WHERE review_job_id = ?", (missing_path["review_job_id"],))
        conn.execute("UPDATE review_jobs SET status = 'running' WHERE review_job_id = ?", (nonqueued["review_job_id"],))
        conn.commit()

    wrong = run_cli(
        "run_review_jobs",
        "--runner",
        "codex",
        "--model",
        "other-model",
        "--review-job-id",
        str(wrong_partition["review_job_id"]),
        cwd=repo,
        db_path=db_path,
        check=False,
    )
    missing = run_cli(
        "run_review_jobs",
        "--runner",
        "codex",
        "--model",
        "test-model",
        "--review-job-id",
        str(missing_path["review_job_id"]),
        cwd=repo,
        db_path=db_path,
        check=False,
    )
    blocked = run_cli(
        "run_review_jobs",
        "--runner",
        "codex",
        "--model",
        "test-model",
        "--review-job-id",
        str(nonqueued["review_job_id"]),
        cwd=repo,
        db_path=db_path,
        check=False,
    )

    assert wrong.returncode == 1
    assert "does not match requested partition" in json.loads(wrong.stdout)["jobs"][0]["failure_reason"]
    assert missing.returncode == 1
    assert "missing load-bearing path" in json.loads(missing.stdout)["jobs"][0]["failure_reason"]
    assert blocked.returncode == 1
    assert "not claimable: running" in json.loads(blocked.stdout)["jobs"][0]["failure_reason"]


def test_run_review_jobs_rejects_unsupported_effort_before_selection(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)

    result = run_cli(
        "run_review_jobs",
        "--runner",
        "codex",
        "--model",
        "test-model",
        "--effort",
        "high",
        cwd=repo,
        db_path=db_path,
        check=False,
    )

    payload = json.loads(result.stdout)
    assert result.returncode == 1
    assert payload["error"] == "runner 'codex' does not support reasoning effort"
    assert payload["selected_count"] == 0
