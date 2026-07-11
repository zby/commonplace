from __future__ import annotations

import json
import sqlite3
import subprocess
import tomllib
from pathlib import Path

from commonplace.lib import frontmatter

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
status: current
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
    return repo, repo / "kb" / "reports" / "review-store.sqlite"


def pair_block(note_path: str, criterion_id: str, body: str, decision: str) -> str:
    return (
        f"=== PAIR REVIEW START: {note_path} :: {criterion_id} ===\n"
        f"{body}\n\n"
        f"## Result: {decision}\n"
        f"=== PAIR REVIEW END: {note_path} :: {criterion_id} ===\n"
    )


def bundle_output() -> str:
    return (
        pair_block("kb/notes/sample.md", GATE_ONE_PATH, "Needs a definition for Alpha.", "WARN")
        + "\n"
        + pair_block("kb/notes/sample.md", GATE_TWO_PATH, "No residue found.", "PASS")
    )


def single_pair_bundle_output() -> str:
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
    assert "runs" not in payload
    jobs = payload["jobs"]
    assert payload["input_mode"] == "selector"
    assert payload["model_partition"] == "test-model"
    assert payload["grouping"] == "note"
    assert payload["created_count"] == 2
    assert payload["skipped_pairs"] == []
    assert [[pair["criterion_path"] for pair in job["pairs"]] for job in jobs] == [[GATE_ONE_PATH], [GATE_TWO_PATH]]

    first_job = jobs[0]
    second_job = jobs[1]
    first_review_job_id = first_job["review_job_id"]
    second_review_job_id = second_job["review_job_id"]
    assert first_job["prompt_path"] == f"kb/reports/bundle-reviews/review-job-{first_review_job_id}/prompt.md"
    assert second_job["prompt_path"] == f"kb/reports/bundle-reviews/review-job-{second_review_job_id}/prompt.md"
    first_manifest_path = f"kb/reports/bundle-reviews/review-job-{first_review_job_id}/MANIFEST.json"

    prompt = (repo / first_job["prompt_path"]).read_text(encoding="utf-8")
    assert f"=== PAIR REVIEW START: kb/notes/sample.md :: {GATE_ONE_PATH} ===" in prompt
    assert f"=== PAIR REVIEW START: kb/notes/sample.md :: {GATE_TWO_PATH} ===" not in prompt
    second_prompt = (repo / second_job["prompt_path"]).read_text(encoding="utf-8")
    assert f"=== PAIR REVIEW START: kb/notes/sample.md :: {GATE_TWO_PATH} ===" in second_prompt

    manifest = json.loads((repo / first_manifest_path).read_text(encoding="utf-8"))
    assert manifest["packing"] == "note"
    assert [pair["result_path"] for pair in manifest["pairs"]] == [
        f"kb/reports/bundle-reviews/review-job-{first_review_job_id}/pair-1-undefined-terms.md",
    ]

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        job_rows = conn.execute(
            """
            SELECT status, runner, runner_model, runner_effort, packing, created_at
            FROM review_jobs
            ORDER BY review_job_id
            """
        ).fetchall()
        assert [(row["status"], row["runner"], row["runner_model"], row["runner_effort"], row["packing"]) for row in job_rows] == [
            ("queued", None, None, None, "note"),
            ("queued", None, None, None, "note"),
        ]
        assert all(row["created_at"] is not None for row in job_rows)
        pair_rows = conn.execute(
            """
            SELECT
                rp.criterion_path,
                rp.reviewed_note_snapshot_id,
                rp.reviewed_criterion_snapshot_id,
                note_snapshot.content_text AS note_text,
                criterion_snapshot.content_text AS criterion_text
            FROM review_pairs AS rp
            JOIN review_file_snapshots AS note_snapshot
              ON rp.reviewed_note_snapshot_id = note_snapshot.snapshot_id
            JOIN review_file_snapshots AS criterion_snapshot
              ON rp.reviewed_criterion_snapshot_id = criterion_snapshot.snapshot_id
            ORDER BY rp.review_job_id, rp.pair_ordinal
            """
        ).fetchall()
        assert [row["criterion_path"] for row in pair_rows] == [
            GATE_ONE_PATH,
            GATE_TWO_PATH,
        ]
        assert {row["reviewed_note_snapshot_id"] for row in pair_rows} != {None}
        assert all(row["reviewed_criterion_snapshot_id"] is not None for row in pair_rows)
        assert all("Term Alpha appears before its definition." in row["note_text"] for row in pair_rows)
        assert all("Fixture gate." in row["criterion_text"] for row in pair_rows)
        job_columns = {row["name"] for row in conn.execute("PRAGMA table_info(review_jobs)").fetchall()}
        pair_columns = {row["name"] for row in conn.execute("PRAGMA table_info(review_pairs)").fetchall()}
        assert "note_path" not in job_columns
        assert "reviewed_note_sha" not in job_columns
        assert "started_at" not in job_columns
        assert "prompt_path" not in job_columns
        assert "bundle_output_path" not in job_columns
        assert "result_path" not in pair_columns


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
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            """
            SELECT snapshot.content_text
            FROM review_pairs AS rp
            JOIN review_file_snapshots AS snapshot
              ON rp.reviewed_criterion_snapshot_id = snapshot.snapshot_id
            WHERE rp.criterion_path = ?
            """,
            (GATE_ONE_PATH,),
        ).fetchone()
    assert row is not None
    assert "Dirty gate marker." in row["content_text"]


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
                        "reason": "missing-review",
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
    assert [job["runner"] for job in list_payload["jobs"]] == [None, None]
    assert [job["runner_model"] for job in list_payload["jobs"]] == [None, None]
    assert [job["pairs"][0]["reviewed_at"] for job in list_payload["jobs"]] == [None, None]


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


def test_public_review_entry_points_replace_ingest_surfaces() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))
    scripts = pyproject["project"]["scripts"]

    assert scripts["commonplace-finalize-review-job"] == "commonplace.cli.review.finalize_review_job:main"
    assert scripts["commonplace-review-target-selector"] == "commonplace.cli.review.review_target_selector:main"
    assert scripts["commonplace-create-review-jobs"] == "commonplace.cli.review.create_review_jobs:main"
    removed_scripts = [
        "commonplace-" + "claim-review-job",
        "commonplace-" + "repair-model-partitions",
        "commonplace-" + "ingest-bundle-output",
        "commonplace-" + "ingest-" + "batch-output",
        "commonplace-" + "run-review-jobs",
        "commonplace-" + "run-review-bundles",
        "commonplace-" + "run-gate-sweep",
        "commonplace-" + "review-sweep",
    ]
    for script_name in removed_scripts:
        assert script_name not in scripts


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
    write(repo / prepared["jobs"][0]["bundle_output_path"], single_pair_bundle_output())

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
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        job = conn.execute("SELECT status, runner, runner_model, runner_effort FROM review_jobs").fetchone()
        pair = conn.execute("SELECT decision FROM review_pairs").fetchone()
        acceptance_count = conn.execute("SELECT COUNT(*) FROM acceptance").fetchone()[0]
    assert (job["status"], job["runner"], job["runner_model"], job["runner_effort"]) == ("queued", None, None, None)
    assert pair["decision"] is None
    assert acceptance_count == 0

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
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        job = conn.execute("SELECT runner, runner_model, runner_effort FROM review_jobs").fetchone()
    assert (job["runner"], job["runner_model"], job["runner_effort"]) == ("external", "unknown-model", "high")


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
    write(repo / prepared_job["bundle_output_path"], single_pair_bundle_output())
    manifest_path = repo / f"kb/reports/bundle-reviews/review-job-{review_job_id}/MANIFEST.json"
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
        "failed": [],
        "job": {"review_job_id": review_job_id, "status": "completed"},
        "review_job_id": review_job_id,
        "state_changed": True,
    }
    result_path = f"kb/reports/bundle-reviews/review-job-{review_job_id}/pair-1-undefined-terms.md"
    result_text = (repo / result_path).read_text(encoding="utf-8")
    parsed_frontmatter = frontmatter.parse(result_text)
    assert parsed_frontmatter.ok
    assert parsed_frontmatter.data["review_job_id"] == review_job_id
    assert parsed_frontmatter.data["note_path"] == "kb/notes/sample.md"
    assert parsed_frontmatter.data["criterion_path"] == GATE_ONE_PATH
    assert parsed_frontmatter.data["model_partition"] == "test-model"
    assert parsed_frontmatter.data["runner"] == "live-agent"
    assert parsed_frontmatter.data["runner_model"] == "test-model"
    assert parsed_frontmatter.data["runner_effort"] is None
    assert "runner_effort: null\n" in result_text
    assert parsed_frontmatter.data["decision"] == "warn"
    assert parsed_frontmatter.data["reviewed_at"] is not None
    assert frontmatter.strip(result_text) == "Needs a definition for Alpha.\n\n## Result: WARN\n"
    refreshed_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert refreshed_manifest["bundle_output_path"] == prepared_job["bundle_output_path"]
    assert refreshed_manifest["pairs"][0]["result_path"] == result_path
    assert refreshed_manifest["pairs"][0]["status"] == "completed"
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute("SELECT decision, reviewed_at FROM review_pairs").fetchone()
    assert parsed_frontmatter.data["decision"] == row["decision"]
    assert parsed_frontmatter.data["reviewed_at"] == row["reviewed_at"]


def test_finalize_review_job_result_write_failure_rolls_back_and_preserves_provenance(
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
    write(repo / prepared_job["bundle_output_path"], single_pair_bundle_output())

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
    assert payload["failed"] == [
        {"review_job_id": review_job_id, "reason": "simulated result write failure"}
    ]
    assert payload["job"] == {"review_job_id": review_job_id, "status": "failed"}
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        job = conn.execute(
            "SELECT status, failure_reason, runner, runner_model, runner_effort FROM review_jobs"
        ).fetchone()
        pair = conn.execute("SELECT decision, reviewed_at FROM review_pairs").fetchone()
        acceptance_count = conn.execute("SELECT COUNT(*) FROM acceptance").fetchone()[0]
    assert (
        job["status"],
        job["failure_reason"],
        job["runner"],
        job["runner_model"],
        job["runner_effort"],
    ) == ("failed", "simulated result write failure", "live-agent", "test-model", None)
    assert (pair["decision"], pair["reviewed_at"]) == (None, None)
    assert acceptance_count == 0

    artifact_dir = repo / "kb" / "reports" / "bundle-reviews" / f"review-job-{review_job_id}"
    assert not (artifact_dir / "pair-1-undefined-terms.md").exists()
    manifest = json.loads((artifact_dir / "MANIFEST.json").read_text(encoding="utf-8"))
    assert manifest["status"] == "failed"
    assert manifest["pairs"][0]["status"] == "failed"


def test_finalize_review_job_finalizes_queued_job(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    prepared = json.loads(
        create_jobs_from_targets(
            repo,
            db_path,
            [target("kb/notes/sample.md", GATE_ONE_PATH, GATE_ONE)],
        ).stdout
    )
    prepared_job = prepared["jobs"][0]
    output_path = repo / prepared_job["bundle_output_path"]
    output_path.write_text(single_pair_bundle_output(), encoding="utf-8")

    result = run_cli(
        "finalize_review_job",
        "--review-job-id",
        str(prepared_job["review_job_id"]),
        cwd=repo,
        db_path=db_path,
    )

    assert json.loads(result.stdout)["completed"] is True
    artifact_dir = repo / "kb" / "reports" / "bundle-reviews" / f"review-job-{prepared_job['review_job_id']}"
    assert frontmatter.strip((artifact_dir / "pair-1-undefined-terms.md").read_text(encoding="utf-8")).strip().endswith("## Result: WARN")
    assert not (artifact_dir / "kb__notes__sample.md :: kb__instructions__review-gates__accessibility__undefined-terms.md").exists()
    manifest = json.loads((artifact_dir / "MANIFEST.json").read_text(encoding="utf-8"))
    assert [pair["status"] for pair in manifest["pairs"]] == ["completed"]
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        job = conn.execute("SELECT status FROM review_jobs").fetchone()
        assert job["status"] == "completed"
        pairs = conn.execute("SELECT criterion_path, decision FROM review_pairs ORDER BY pair_ordinal").fetchall()
        assert [(row["criterion_path"], row["decision"]) for row in pairs] == [
            (GATE_ONE_PATH, "warn"),
        ]
        snapshot_rows = conn.execute(
            """
            SELECT
                rp.reviewed_note_snapshot_id,
                rp.reviewed_criterion_snapshot_id,
                ae.accepted_note_snapshot_id,
                ae.accepted_criterion_snapshot_id
            FROM review_pairs AS rp
            JOIN acceptance AS ae
              ON ae.accepted_review_pair_id = rp.review_pair_id
            ORDER BY rp.pair_ordinal
            """
        ).fetchall()
        assert [
            (
                row["accepted_note_snapshot_id"] == row["reviewed_note_snapshot_id"],
                row["accepted_criterion_snapshot_id"] == row["reviewed_criterion_snapshot_id"],
            )
            for row in snapshot_rows
        ] == [(True, True)]
        assert conn.execute("SELECT COUNT(*) FROM acceptance").fetchone()[0] == 1


def test_failed_rereview_preserves_previous_acceptance_and_artifacts(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    first_job = create_single_review_job(repo, db_path)
    first_job_id = int(first_job["review_job_id"])
    write(repo / str(first_job["bundle_output_path"]), single_pair_bundle_output())

    first_result = run_cli(
        "finalize_review_job",
        "--review-job-id",
        str(first_job_id),
        cwd=repo,
        db_path=db_path,
    )
    assert json.loads(first_result.stdout)["completed"] is True
    first_artifact_dir = repo / "kb" / "reports" / "bundle-reviews" / f"review-job-{first_job_id}"

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        first_pair_id = conn.execute(
            "SELECT review_pair_id FROM review_pairs WHERE review_job_id = ?",
            (first_job_id,),
        ).fetchone()["review_pair_id"]

    write(repo / "kb" / "notes" / "sample.md", "---\ndescription: Test note\ntype: kb/types/note.md\ntraits: []\nstatus: current\n---\n\n# Test note\n\nChanged body.\n")
    second_job = create_single_review_job(repo, db_path)
    second_job_id = int(second_job["review_job_id"])
    write(repo / str(second_job["bundle_output_path"]), "not a valid bundle\n")

    failed = run_cli(
        "finalize_review_job",
        "--review-job-id",
        str(second_job_id),
        cwd=repo,
        db_path=db_path,
        check=False,
    )

    assert failed.returncode == 1
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        current_acceptance = conn.execute(
            """
            SELECT accepted_review_pair_id
            FROM current_criterion_acceptances
            WHERE note_path = ? AND criterion_path = ? AND model_partition = ?
            """,
            ("kb/notes/sample.md", GATE_ONE_PATH, "test-model"),
        ).fetchone()
        first_job_status = conn.execute(
            "SELECT status FROM review_jobs WHERE review_job_id = ?",
            (first_job_id,),
        ).fetchone()["status"]
        second_job_status = conn.execute(
            "SELECT status FROM review_jobs WHERE review_job_id = ?",
            (second_job_id,),
        ).fetchone()["status"]

    assert current_acceptance["accepted_review_pair_id"] == first_pair_id
    assert first_job_status == "completed"
    assert second_job_status == "failed"
    assert first_artifact_dir.exists()


def test_successful_rereview_prunes_superseded_job_and_artifacts(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    first_job = create_single_review_job(repo, db_path)
    first_job_id = int(first_job["review_job_id"])
    write(repo / str(first_job["bundle_output_path"]), single_pair_bundle_output())
    run_cli(
        "finalize_review_job",
        "--review-job-id",
        str(first_job_id),
        cwd=repo,
        db_path=db_path,
    )
    first_artifact_dir = repo / "kb" / "reports" / "bundle-reviews" / f"review-job-{first_job_id}"
    assert first_artifact_dir.exists()
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        first_pair_id = conn.execute(
            "SELECT review_pair_id FROM review_pairs WHERE review_job_id = ?",
            (first_job_id,),
        ).fetchone()["review_pair_id"]

    write(repo / "kb" / "notes" / "sample.md", "---\ndescription: Test note\ntype: kb/types/note.md\ntraits: []\nstatus: current\n---\n\n# Test note\n\nChanged body.\n")
    second_job = create_single_review_job(repo, db_path)
    second_job_id = int(second_job["review_job_id"])
    write(repo / str(second_job["bundle_output_path"]), single_pair_bundle_output())

    second_result = run_cli(
        "finalize_review_job",
        "--review-job-id",
        str(second_job_id),
        cwd=repo,
        db_path=db_path,
    )

    assert json.loads(second_result.stdout)["completed"] is True
    second_artifact_dir = repo / "kb" / "reports" / "bundle-reviews" / f"review-job-{second_job_id}"
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        current_acceptance = conn.execute(
            """
            SELECT accepted_review_pair_id
            FROM current_criterion_acceptances
            WHERE note_path = ? AND criterion_path = ? AND model_partition = ?
            """,
            ("kb/notes/sample.md", GATE_ONE_PATH, "test-model"),
        ).fetchone()
        first_pair = conn.execute(
            "SELECT review_pair_id FROM review_pairs WHERE review_pair_id = ?",
            (first_pair_id,),
        ).fetchone()
        first_job_row = conn.execute(
            "SELECT review_job_id FROM review_jobs WHERE review_job_id = ?",
            (first_job_id,),
        ).fetchone()
        acceptance_count = conn.execute("SELECT COUNT(*) FROM acceptance").fetchone()[0]

    assert current_acceptance["accepted_review_pair_id"] != first_pair_id
    assert first_pair is None
    assert first_job_row is None
    assert acceptance_count == 1
    assert not first_artifact_dir.exists()
    assert second_artifact_dir.exists()
