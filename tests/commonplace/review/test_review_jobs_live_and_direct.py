from __future__ import annotations

import json
import subprocess
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.review import review_target_selector

from ._run_cli import run_cli

GATE_ONE = "accessibility/undefined-terms"
GATE_TWO = "prose/source-residue"
GATE_ONE_PATH = "kb/instructions/review-gates/accessibility/undefined-terms.md"
GATE_TWO_PATH = "kb/instructions/review-gates/prose/source-residue.md"
INSTALLED_GATE_ONE_PATH = "kb/commonplace/instructions/review-gates/accessibility/undefined-terms.md"


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
---

# Test note

Term Alpha appears before its definition.
""",
    )


def make_gate(path: Path, criterion_id: str, lens: str) -> Path:
    return write(
        path,
        f"""---
gate_id: {criterion_id}
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


def build_repo_fixture(
    tmp_path: Path,
    *,
    gates_root: Path = Path("kb/instructions/review-gates"),
) -> tuple[Path, Path]:
    repo = tmp_path / "repo"
    repo.mkdir()
    init_repo(repo)
    make_note(repo / "kb" / "notes" / "sample.md")
    make_gate(
        repo / gates_root / "accessibility" / "undefined-terms.md",
        GATE_ONE,
        "accessibility",
    )
    make_gate(
        repo / gates_root / "prose" / "source-residue.md",
        GATE_TWO,
        "prose",
    )
    commit_all(repo, "fixture")
    return repo, repo / "kb" / "reports" / "commonplace-store.sqlite"


def pair_block(note_path: str, criterion_id: str, body: str, outcome: str) -> str:
    return (
        f"=== PAIR REVIEW START: {note_path} :: {criterion_id} ===\n"
        f"{body}\n\n"
        f"## Result: {outcome}\n"
        f"=== PAIR REVIEW END: {note_path} :: {criterion_id} ===\n"
    )


def job_output() -> str:
    return (
        pair_block("kb/notes/sample.md", GATE_ONE_PATH, "Needs a definition for Alpha.", "WARN")
        + "\n"
        + pair_block("kb/notes/sample.md", GATE_TWO_PATH, "No residue found.", "PASS")
    )


def single_pair_job_output() -> str:
    return pair_block("kb/notes/sample.md", GATE_ONE_PATH, "Needs a definition for Alpha.", "WARN")


def create_single_review_job(repo: Path, db_path: Path) -> dict[str, object]:
    prepared = json.loads(
        create_jobs_from_targets(
            repo,
            db_path,
            [target("kb/notes/sample.md", GATE_ONE_PATH, GATE_ONE)],
        ).stdout
    )
    return prepared["jobs"][0]


def create_jobs_from_targets(
    repo: Path,
    db_path: Path,
    targets: list[dict[str, str]],
    *,
    grouping: str = "note",
    model: str = "test-model",
    batch_size: int | None = None,
):
    selector_path = repo / "targets.json"
    selector_path.write_text(
        json.dumps({"model_partition": model, "targets": targets}),
        encoding="utf-8",
    )
    args = ["--input", "targets.json", "--grouping", grouping]
    if batch_size is not None:
        args.extend(["--batch-size", str(batch_size)])
    return run_cli("create_review_jobs", *args, cwd=repo, db_path=db_path)


def target(note_path: str, criterion_path: str, criterion_id: str, reason: str = "requested") -> dict[str, str]:
    return {
        "note_path": note_path,
        "criterion_path": criterion_path,
        "criterion_id": criterion_id,
        "reason": reason,
    }


def test_create_review_jobs_groups_cross_lens_gates_by_bundle(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)

    result = create_jobs_from_targets(
        repo,
        db_path,
        [
            target("kb/notes/sample.md", GATE_ONE_PATH, GATE_ONE),
            target("kb/notes/sample.md", GATE_TWO_PATH, GATE_TWO),
        ],
    )

    payload = json.loads(result.stdout)
    jobs = payload["jobs"]
    assert {
        "input_mode": payload["input_mode"],
        "model_partition": payload["model_partition"],
        "grouping": payload["grouping"],
        "created_count": payload["created_count"],
        "skipped_pairs": payload["skipped_pairs"],
    } == {
        "input_mode": "selector",
        "model_partition": "test-model",
        "grouping": "note",
        "created_count": 2,
        "skipped_pairs": [],
    }
    assert [[pair["criterion_path"] for pair in job["pairs"]] for job in jobs] == [[GATE_ONE_PATH], [GATE_TWO_PATH]]

    first_job = jobs[0]
    second_job = jobs[1]
    first_review_job_id = first_job["review_job_id"]
    second_review_job_id = second_job["review_job_id"]
    assert first_job["prompt_path"] == f"kb/reports/review-jobs/review-job-{first_review_job_id}/prompt.md"
    assert second_job["prompt_path"] == f"kb/reports/review-jobs/review-job-{second_review_job_id}/prompt.md"
    first_manifest_path = f"kb/reports/review-jobs/review-job-{first_review_job_id}/MANIFEST.json"

    prompt = (repo / first_job["prompt_path"]).read_text(encoding="utf-8")
    assert f"=== PAIR REVIEW START: kb/notes/sample.md :: {GATE_ONE_PATH} ===" in prompt
    assert f"=== PAIR REVIEW START: kb/notes/sample.md :: {GATE_TWO_PATH} ===" not in prompt
    second_prompt = (repo / second_job["prompt_path"]).read_text(encoding="utf-8")
    assert f"=== PAIR REVIEW START: kb/notes/sample.md :: {GATE_TWO_PATH} ===" in second_prompt

    manifest = json.loads((repo / first_manifest_path).read_text(encoding="utf-8"))
    assert manifest["grouping"] == "note"
    assert [pair["result_path"] for pair in manifest["pairs"]] == [
        f"kb/reports/review-jobs/review-job-{first_review_job_id}/pair-1-undefined-terms.md",
    ]


def test_create_review_jobs_snapshots_dirty_criterion_text(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    dirty_criterion_text = """---
gate_id: accessibility/undefined-terms
name: Undefined Terms
lens: accessibility
watches: [body]
staleness: changed
---

## Failure mode

Dirty gate marker.
"""
    (repo / GATE_ONE_PATH).write_text(dirty_criterion_text, encoding="utf-8")

    result = create_jobs_from_targets(
        repo,
        db_path,
        [target("kb/notes/sample.md", GATE_ONE_PATH, GATE_ONE)],
    )

    payload = json.loads(result.stdout)
    prompt = (repo / payload["jobs"][0]["prompt_path"]).read_text(encoding="utf-8")
    assert "Dirty gate marker." in prompt


def test_create_review_jobs_resolves_installed_commonplace_gates(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(
        tmp_path,
        gates_root=Path("kb/commonplace/instructions/review-gates"),
    )

    result = create_jobs_from_targets(
        repo,
        db_path,
        [target("kb/notes/sample.md", INSTALLED_GATE_ONE_PATH, GATE_ONE)],
    )

    payload = json.loads(result.stdout)
    assert [pair["criterion_path"] for pair in payload["jobs"][0]["pairs"]] == [INSTALLED_GATE_ONE_PATH]


def test_create_review_jobs_accepts_selector_json_file_and_validates_model(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    selector_path = repo / "targets.json"
    selector_path.write_text(
        json.dumps(
            {
                "model_partition": "test-model",
                "targets": [
                    {
                        "note_path": "kb/notes/sample.md",
                        "criterion_path": GATE_ONE_PATH,
                        "criterion_id": GATE_ONE,
                        "reason": "missing-baseline",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    result = run_cli(
        "create_review_jobs",
        "--input",
        "targets.json",
        "--model-partition",
        "test-model",
        "--grouping",
        "note",
        cwd=repo,
        db_path=db_path,
    )

    payload = json.loads(result.stdout)
    assert payload["input_mode"] == "selector"
    assert payload["created_count"] == 1
    assert payload["jobs"][0]["pairs"][0]["criterion_id"] == GATE_ONE

    mismatch = run_cli(
        "create_review_jobs",
        "--input",
        "targets.json",
        "--model-partition",
        "other-model",
        "--grouping",
        "note",
        cwd=repo,
        db_path=db_path,
        check=False,
    )
    assert mismatch.returncode == 2
    assert "does not match selector model_partition" in mismatch.stderr


def test_create_review_jobs_selector_noop_and_model_agnostic_input(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    selector_path = repo / "empty-targets.json"
    selector_path.write_text(json.dumps({"model_partition": "test-model", "targets": []}), encoding="utf-8")

    result = run_cli(
        "create_review_jobs",
        "--input",
        "empty-targets.json",
        "--grouping",
        "criterion",
        cwd=repo,
        db_path=db_path,
    )

    payload = json.loads(result.stdout)
    assert payload["created_count"] == 0
    assert payload["jobs"] == []
    assert payload["skipped_pairs"] == []

    selector_path.write_text(json.dumps({"model_partition": None, "targets": []}), encoding="utf-8")
    accepted = run_cli(
        "create_review_jobs",
        "--input",
        "empty-targets.json",
        "--model-partition",
        "test-model",
        "--grouping",
        "note",
        cwd=repo,
        db_path=db_path,
    )
    payload = json.loads(accepted.stdout)
    assert payload["model_partition"] == "test-model"
    assert payload["created_count"] == 0
    assert payload["jobs"] == []

    rejected = run_cli(
        "create_review_jobs",
        "--input",
        "empty-targets.json",
        "--grouping",
        "note",
        cwd=repo,
        db_path=db_path,
        check=False,
    )
    assert rejected.returncode == 2
    assert "model_partition is required" in rejected.stderr


def test_create_review_jobs_selector_criterion_grouping_chunks_and_lists(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    make_note(repo / "kb" / "notes" / "other.md")

    result = create_jobs_from_targets(
        repo,
        db_path,
        [
            target("kb/notes/sample.md", GATE_ONE_PATH, GATE_ONE),
            target("kb/notes/other.md", GATE_ONE_PATH, GATE_ONE),
            target("kb/notes/sample.md", GATE_ONE_PATH, GATE_ONE),
        ],
        grouping="criterion",
        batch_size=1,
    )

    payload = json.loads(result.stdout)
    assert payload["input_mode"] == "selector"
    assert payload["created_count"] == 2
    assert payload["skipped_pairs"] == [
        {
            "note_path": "kb/notes/sample.md",
            "criterion_path": GATE_ONE_PATH,
            "criterion_id": GATE_ONE,
            "reason": "duplicate",
        }
    ]
    assert [[pair["result_path"].split("/")[-1] for pair in job["pairs"]] for job in payload["jobs"]] == [
        ["pair-1-sample.md"],
        ["pair-1-other.md"],
    ]

    listed = run_cli(
        "review_job_list",
        "--status",
        "queued",
        "--json",
        cwd=repo,
        db_path=db_path,
    )
    list_payload = json.loads(listed.stdout)
    assert list_payload["filters"] == {"model_partition": None, "status": "queued"}
    assert list_payload["count"] == 2


def test_create_review_jobs_rejects_batch_size_with_note_grouping(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    selector_path = repo / "targets.json"
    selector_path.write_text(
        json.dumps(
            {
                "model_partition": "test-model",
                "targets": [target("kb/notes/sample.md", GATE_ONE_PATH, GATE_ONE)],
            }
        ),
        encoding="utf-8",
    )

    result = run_cli(
        "create_review_jobs",
        "--input",
        "targets.json",
        "--grouping",
        "note",
        "--batch-size",
        "2",
        cwd=repo,
        db_path=db_path,
        check=False,
    )

    assert result.returncode == 2
    assert "--batch-size is only valid with --grouping criterion" in result.stderr


def test_finalize_review_job_validates_model_effort_partition_before_mutation(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    prepared = json.loads(
        create_jobs_from_targets(
            repo,
            db_path,
            [target("kb/notes/sample.md", GATE_ONE_PATH, GATE_ONE)],
            model="unknown-model-high",
        ).stdout
    )
    review_job_id = prepared["jobs"][0]["review_job_id"]
    write(repo / prepared["jobs"][0]["job_output_path"], single_pair_job_output())

    rejected = run_cli(
        "finalize_review_job",
        "--review-job-id",
        str(review_job_id),
        "--model",
        "unknown-model",
        cwd=repo,
        db_path=db_path,
        check=False,
    )
    assert rejected.returncode == 1
    payload = json.loads(rejected.stdout)
    assert "does not match supplied partition" in payload["reason"]
    assert payload["state_changed"] is False

    accepted = run_cli(
        "finalize_review_job",
        "--review-job-id",
        str(review_job_id),
        "--runner",
        "external",
        "--model",
        "unknown-model",
        "--effort",
        "high",
        cwd=repo,
        db_path=db_path,
    )
    payload = json.loads(accepted.stdout)
    assert payload["completed"] is True


def test_finalize_review_job_uses_job_owned_paths_and_writes_provenance_frontmatter(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    prepared = json.loads(
        create_jobs_from_targets(
            repo,
            db_path,
            [target("kb/notes/sample.md", GATE_ONE_PATH, GATE_ONE)],
        ).stdout
    )
    prepared_job = prepared["jobs"][0]
    review_job_id = prepared_job["review_job_id"]
    write(repo / prepared_job["job_output_path"], single_pair_job_output())
    manifest_path = repo / f"kb/reports/review-jobs/review-job-{review_job_id}/MANIFEST.json"
    manifest_path.write_text("{not valid json", encoding="utf-8")

    result = run_cli(
        "finalize_review_job",
        "--review-job-id",
        str(review_job_id),
        "--runner",
        "live-agent",
        "--model",
        "test-model",
        cwd=repo,
        db_path=db_path,
    )

    payload = json.loads(result.stdout)
    assert payload == {
        "completed": True,
        "completed_pair_count": 1,
        "failure_reason": None,
        "job": {"review_job_id": review_job_id, "status": "completed"},
        "review_job_id": review_job_id,
        "state_changed": True,
    }
    result_path = f"kb/reports/review-jobs/review-job-{review_job_id}/pair-1-undefined-terms.md"
    result_text = (repo / result_path).read_text(encoding="utf-8")
    parsed_frontmatter = frontmatter.parse(result_text)
    assert {
        key: parsed_frontmatter.data[key]
        for key in (
            "review_job_id",
            "note_path",
            "criterion_path",
            "model_partition",
            "runner",
            "runner_model",
            "outcome",
        )
    } == {
        "review_job_id": review_job_id,
        "note_path": "kb/notes/sample.md",
        "criterion_path": GATE_ONE_PATH,
        "model_partition": "test-model",
        "runner": "live-agent",
        "runner_model": "test-model",
        "outcome": "warn",
    }
    assert parsed_frontmatter.data["completed_at"] is not None
    assert frontmatter.strip(result_text) == "Needs a definition for Alpha.\n\n## Result: WARN\n"
    refreshed_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert refreshed_manifest["job_output_path"] == prepared_job["job_output_path"]
    assert refreshed_manifest["pairs"][0]["result_path"] == result_path
    assert refreshed_manifest["pairs"][0]["status"] == "completed"


def test_finalize_review_job_preserves_optional_self_reported_model(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    prepared_job = create_single_review_job(repo, db_path)
    review_job_id = prepared_job["review_job_id"]
    write(
        repo / prepared_job["job_output_path"],
        "self-reported-model: gpt-5.6-sol\n\n" + single_pair_job_output(),
    )

    result = run_cli(
        "finalize_review_job",
        "--review-job-id",
        str(review_job_id),
        cwd=repo,
        db_path=db_path,
    )

    payload = json.loads(result.stdout)
    assert payload["self_reported_model"] == "gpt-5.6-sol"
    result_path = repo / (
        f"kb/reports/review-jobs/review-job-{review_job_id}/"
        "pair-1-undefined-terms.md"
    )
    parsed_frontmatter = frontmatter.parse(result_path.read_text(encoding="utf-8"))
    assert parsed_frontmatter.data["self-reported-model"] == "gpt-5.6-sol"
    assert parsed_frontmatter.data["runner_model"] is None


def test_finalize_review_job_result_write_failure_leaves_no_result_artifact(
    tmp_path: Path,
    monkeypatch,
) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    prepared = json.loads(
        create_jobs_from_targets(
            repo,
            db_path,
            [target("kb/notes/sample.md", GATE_ONE_PATH, GATE_ONE)],
        ).stdout
    )
    prepared_job = prepared["jobs"][0]
    review_job_id = prepared_job["review_job_id"]
    write(repo / prepared_job["job_output_path"], single_pair_job_output())

    from commonplace.review import finalization

    def fail_result_write(**_kwargs):
        raise OSError("simulated result write failure")

    monkeypatch.setattr(finalization, "write_pair_result_files_to_derived_paths", fail_result_write)

    result = run_cli(
        "finalize_review_job",
        "--review-job-id",
        str(review_job_id),
        "--runner",
        "live-agent",
        "--model",
        "test-model",
        cwd=repo,
        db_path=db_path,
        check=False,
    )

    assert result.returncode == 1
    payload = json.loads(result.stdout)
    assert payload["completed"] is False
    assert payload["completed_pair_count"] == 0
    assert payload["failure_reason"] == "simulated result write failure"
    assert payload["job"] == {"review_job_id": review_job_id, "status": "failed"}

    artifact_dir = repo / "kb" / "reports" / "review-jobs" / f"review-job-{review_job_id}"
    assert not (artifact_dir / "pair-1-undefined-terms.md").exists()
    manifest = json.loads((artifact_dir / "MANIFEST.json").read_text(encoding="utf-8"))
    assert manifest["status"] == "failed"
    assert manifest["pairs"][0]["status"] == "failed"


def test_failed_rereview_preserves_previous_freshness_baseline_and_artifacts(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    first_job = create_single_review_job(repo, db_path)
    first_job_id = int(first_job["review_job_id"])
    write(repo / str(first_job["job_output_path"]), single_pair_job_output())

    first_result = run_cli(
        "finalize_review_job",
        "--review-job-id",
        str(first_job_id),
        cwd=repo,
        db_path=db_path,
    )
    assert json.loads(first_result.stdout)["completed"] is True
    first_artifact_dir = repo / "kb" / "reports" / "review-jobs" / f"review-job-{first_job_id}"

    write(repo / "kb" / "notes" / "sample.md", "---\ndescription: Test note\ntype: kb/types/note.md\ntraits: []\n---\n\n# Test note\n\nChanged body.\n")
    second_job = create_single_review_job(repo, db_path)
    second_job_id = int(second_job["review_job_id"])
    write(repo / str(second_job["job_output_path"]), "not a valid bundle\n")

    failed = run_cli(
        "finalize_review_job",
        "--review-job-id",
        str(second_job_id),
        cwd=repo,
        db_path=db_path,
        check=False,
    )

    assert failed.returncode == 1
    assert json.loads(failed.stdout)["completed"] is False
    assert first_artifact_dir.exists()
    stale = review_target_selector.select_stale_criteria(
        repo,
        model="test-model",
        criterion_ids=[GATE_ONE],
        note_filter=["kb/notes/sample.md"],
        db_path=db_path,
    )
    assert [record.reason for record in stale] == ["note-changed"]


def test_successful_rereview_prunes_superseded_job_and_artifacts(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    first_job = create_single_review_job(repo, db_path)
    first_job_id = int(first_job["review_job_id"])
    write(repo / str(first_job["job_output_path"]), single_pair_job_output())
    run_cli(
        "finalize_review_job",
        "--review-job-id",
        str(first_job_id),
        cwd=repo,
        db_path=db_path,
    )
    first_artifact_dir = repo / "kb" / "reports" / "review-jobs" / f"review-job-{first_job_id}"
    assert first_artifact_dir.exists()

    write(repo / "kb" / "notes" / "sample.md", "---\ndescription: Test note\ntype: kb/types/note.md\ntraits: []\n---\n\n# Test note\n\nChanged body.\n")
    second_job = create_single_review_job(repo, db_path)
    second_job_id = int(second_job["review_job_id"])
    write(repo / str(second_job["job_output_path"]), single_pair_job_output())

    second_result = run_cli(
        "finalize_review_job",
        "--review-job-id",
        str(second_job_id),
        cwd=repo,
        db_path=db_path,
    )

    assert json.loads(second_result.stdout)["completed"] is True
    second_artifact_dir = repo / "kb" / "reports" / "review-jobs" / f"review-job-{second_job_id}"
    assert not first_artifact_dir.exists()
    assert second_artifact_dir.exists()
    stale = review_target_selector.select_stale_criteria(
        repo,
        model="test-model",
        criterion_ids=[GATE_ONE],
        note_filter=["kb/notes/sample.md"],
        db_path=db_path,
    )
    assert stale == []
