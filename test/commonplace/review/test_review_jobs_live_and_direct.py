from __future__ import annotations

import json
import sqlite3
import subprocess
import tomllib
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.review import run_review_jobs as run_review_jobs_lib
from commonplace.review.runners import RunnerResult

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


def pair_block(note_path: str, gate_id: str, body: str, decision: str) -> str:
    return (
        f"=== PAIR REVIEW START: {note_path} :: {gate_id} ===\n"
        f"{body}\n\n"
        f"## Result: {decision}\n"
        f"=== PAIR REVIEW END: {note_path} :: {gate_id} ===\n"
    )


def bundle_output() -> str:
    return (
        pair_block("kb/notes/sample.md", GATE_ONE_PATH, "Needs a definition for Alpha.", "WARN")
        + "\n"
        + pair_block("kb/notes/sample.md", GATE_TWO_PATH, "No residue found.", "PASS")
    )


def single_pair_bundle_output() -> str:
    return pair_block("kb/notes/sample.md", GATE_ONE_PATH, "Needs a definition for Alpha.", "WARN")


def test_create_review_jobs_groups_cross_lens_gates_by_bundle(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)

    result = run_cli(
        "create_review_jobs",
        "--note",
        "kb/notes/sample.md",
        GATE_ONE,
        GATE_TWO,
        "--model",
        "test-model",
        "--grouping",
        "note",
        cwd=repo,
        db_path=db_path,
    )

    payload = json.loads(result.stdout)
    assert "runs" not in payload
    jobs = payload["jobs"]
    assert payload["input_mode"] == "direct-note"
    assert payload["model_partition"] == "test-model"
    assert payload["grouping"] == "note"
    assert payload["created_count"] == 2
    assert payload["skipped_pairs"] == []
    assert [[pair["gate_path"] for pair in job["pairs"]] for job in jobs] == [[GATE_ONE_PATH], [GATE_TWO_PATH]]

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
        f"kb/reports/bundle-reviews/review-job-{first_review_job_id}/undefined-terms.md",
    ]

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        job_rows = conn.execute(
            """
            SELECT status, runner, runner_model, runner_effort, packing, created_at, started_at, prompt_path, bundle_output_path
            FROM review_jobs
            ORDER BY review_job_id
            """
        ).fetchall()
        assert [(row["status"], row["runner"], row["runner_model"], row["runner_effort"], row["packing"]) for row in job_rows] == [
            ("queued", None, None, None, "note"),
            ("queued", None, None, None, "note"),
        ]
        assert [row["started_at"] for row in job_rows] == [None, None]
        assert all(row["created_at"] is not None for row in job_rows)
        assert job_rows[0]["prompt_path"] == first_job["prompt_path"]
        assert job_rows[1]["prompt_path"] == second_job["prompt_path"]
        assert job_rows[0]["bundle_output_path"] == first_job["bundle_output_path"]
        assert job_rows[1]["bundle_output_path"] == second_job["bundle_output_path"]
        pair_rows = conn.execute(
            """
            SELECT
                rp.gate_path,
                rp.pair_status,
                rp.result_path,
                rp.reviewed_note_snapshot_id,
                rp.reviewed_gate_snapshot_id,
                note_snapshot.content_text AS note_text,
                gate_snapshot.content_text AS gate_text
            FROM review_pairs AS rp
            JOIN review_file_snapshots AS note_snapshot
              ON rp.reviewed_note_snapshot_id = note_snapshot.snapshot_id
            JOIN review_file_snapshots AS gate_snapshot
              ON rp.reviewed_gate_snapshot_id = gate_snapshot.snapshot_id
            ORDER BY rp.review_job_id, rp.pair_ordinal
            """
        ).fetchall()
        assert [(row["gate_path"], row["pair_status"]) for row in pair_rows] == [
            (GATE_ONE_PATH, "pending"),
            (GATE_TWO_PATH, "pending"),
        ]
        assert pair_rows[0]["result_path"] == manifest["pairs"][0]["result_path"]
        assert {row["reviewed_note_snapshot_id"] for row in pair_rows} != {None}
        assert all(row["reviewed_gate_snapshot_id"] is not None for row in pair_rows)
        assert all("Term Alpha appears before its definition." in row["note_text"] for row in pair_rows)
        assert all("Fixture gate." in row["gate_text"] for row in pair_rows)
        run_columns = {row["name"] for row in conn.execute("PRAGMA table_info(review_jobs)").fetchall()}
        assert "note_path" not in run_columns
        assert "reviewed_note_sha" not in run_columns


def test_create_review_jobs_snapshots_dirty_gate_text(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    dirty_gate_text = """---
gate_id: accessibility/undefined-terms
name: Undefined Terms
lens: accessibility
watches: [body]
staleness: changed
---

## Failure mode

Dirty gate marker.
"""
    (repo / GATE_ONE_PATH).write_text(dirty_gate_text, encoding="utf-8")

    result = run_cli(
        "create_review_jobs",
        "--note",
        "kb/notes/sample.md",
        GATE_ONE,
        "--model",
        "test-model",
        "--grouping",
        "note",
        cwd=repo,
        db_path=db_path,
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
              ON rp.reviewed_gate_snapshot_id = snapshot.snapshot_id
            WHERE rp.gate_path = ?
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

    result = run_cli(
        "create_review_jobs",
        "--note",
        "kb/notes/sample.md",
        GATE_ONE,
        "--model",
        "test-model",
        "--grouping",
        "note",
        cwd=repo,
        db_path=db_path,
    )

    payload = json.loads(result.stdout)
    assert [pair["gate_path"] for pair in payload["jobs"][0]["pairs"]] == [INSTALLED_GATE_ONE_PATH]


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
                        "gate_path": GATE_ONE_PATH,
                        "gate_id": GATE_ONE,
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
        "--model",
        "test-model",
        "--grouping",
        "note",
        cwd=repo,
        db_path=db_path,
    )

    payload = json.loads(result.stdout)
    assert payload["input_mode"] == "selector"
    assert payload["created_count"] == 1
    assert payload["jobs"][0]["pairs"][0]["gate_id"] == GATE_ONE

    mismatch = run_cli(
        "create_review_jobs",
        "--input",
        "targets.json",
        "--model",
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
        "gate",
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
        "--model",
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


def test_create_review_jobs_direct_pairs_gate_grouping_chunks_and_lists(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    make_note(repo / "kb" / "notes" / "other.md")

    result = run_cli(
        "create_review_jobs",
        "--pair",
        f"kb/notes/sample.md::{GATE_ONE}",
        "--pair",
        f"kb/notes/other.md::{GATE_ONE_PATH}",
        "--pair",
        f"kb/notes/sample.md::{GATE_ONE_PATH}",
        "--model",
        "test-model",
        "--grouping",
        "gate",
        "--batch-size",
        "1",
        cwd=repo,
        db_path=db_path,
    )

    payload = json.loads(result.stdout)
    assert payload["input_mode"] == "direct-pair"
    assert payload["created_count"] == 2
    assert payload["skipped_pairs"] == [
        {
            "note_path": "kb/notes/sample.md",
            "gate_path": GATE_ONE_PATH,
            "gate_id": GATE_ONE,
            "reason": "duplicate",
        }
    ]
    assert [[pair["result_path"].split("/")[-1] for pair in job["pairs"]] for job in payload["jobs"]] == [
        ["sample.md"],
        ["other.md"],
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

    result = run_cli(
        "create_review_jobs",
        "--note",
        "kb/notes/sample.md",
        GATE_ONE,
        "--model",
        "test-model",
        "--grouping",
        "note",
        "--batch-size",
        "2",
        cwd=repo,
        db_path=db_path,
        check=False,
    )

    assert result.returncode == 2
    assert "--batch-size is only valid with --grouping gate" in result.stderr


def test_public_review_entry_points_replace_ingest_surfaces() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))
    scripts = pyproject["project"]["scripts"]

    assert scripts["commonplace-claim-review-job"] == "commonplace.cli.review.claim_review_job:main"
    assert scripts["commonplace-finalize-review-job"] == "commonplace.cli.review.finalize_review_job:main"
    assert scripts["commonplace-run-review-jobs"] == "commonplace.cli.review.run_review_jobs:main"
    assert "commonplace-ingest-bundle-output" not in scripts
    assert "commonplace-ingest-batch-output" not in scripts


def test_claim_review_job_records_dispatch_provenance_and_rejects_second_claim(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    prepared = json.loads(
        run_cli(
            "create_review_jobs",
            "--note",
            "kb/notes/sample.md",
            GATE_ONE,
            "--model",
            "test-model",
            "--grouping",
            "note",
            cwd=repo,
            db_path=db_path,
        ).stdout
    )
    prepared_job = prepared["jobs"][0]

    claimed = run_cli(
        "claim_review_job",
        "--review-job-id",
        str(prepared_job["review_job_id"]),
        "--runner",
        "codex",
        "--model",
        "test-model",
        cwd=repo,
        db_path=db_path,
    )

    claim_payload = json.loads(claimed.stdout)
    assert claim_payload["claimed"] is True
    assert claim_payload["job"]["status"] == "running"
    assert claim_payload["job"]["runner"] == "codex"
    assert claim_payload["job"]["runner_model"] == "test-model"
    assert claim_payload["job"]["runner_effort"] is None
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        job = conn.execute("SELECT status, started_at, runner, runner_model, runner_effort FROM review_jobs").fetchone()
        assert job["status"] == "running"
        assert job["started_at"] is not None
        assert job["runner"] == "codex"
        assert job["runner_model"] == "test-model"
        assert job["runner_effort"] is None

    rejected = run_cli(
        "claim_review_job",
        "--review-job-id",
        str(prepared_job["review_job_id"]),
        "--runner",
        "codex",
        "--model",
        "test-model",
        cwd=repo,
        db_path=db_path,
        check=False,
    )
    assert rejected.returncode == 1
    rejected_payload = json.loads(rejected.stdout)
    assert rejected_payload == {
        "claimed": False,
        "reason": "review job is not claimable: running",
        "review_job_id": prepared_job["review_job_id"],
    }


def test_claim_review_job_validates_model_effort_partition(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    prepared = json.loads(
        run_cli(
            "create_review_jobs",
            "--note",
            "kb/notes/sample.md",
            GATE_ONE,
            "--model",
            "unknown-model-high",
            "--grouping",
            "note",
            cwd=repo,
            db_path=db_path,
        ).stdout
    )
    review_job_id = prepared["jobs"][0]["review_job_id"]

    rejected = run_cli(
        "claim_review_job",
        "--review-job-id",
        str(review_job_id),
        "--runner",
        "external",
        "--model",
        "unknown-model",
        cwd=repo,
        db_path=db_path,
        check=False,
    )
    assert rejected.returncode == 1
    assert "does not match claimed partition" in json.loads(rejected.stdout)["reason"]

    claimed = run_cli(
        "claim_review_job",
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
    payload = json.loads(claimed.stdout)
    assert payload["claimed"] is True
    assert payload["job"]["runner_effort"] == "high"


def test_finalize_review_job_uses_job_owned_paths_and_writes_provenance_frontmatter(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    prepared = json.loads(
        run_cli(
            "create_review_jobs",
            "--note",
            "kb/notes/sample.md",
            GATE_ONE,
            "--model",
            "test-model",
            "--grouping",
            "note",
            cwd=repo,
            db_path=db_path,
        ).stdout
    )
    prepared_job = prepared["jobs"][0]
    review_job_id = prepared_job["review_job_id"]
    custom_output = "kb/reports/custom-review-output/job-output.md"
    custom_result = "kb/reports/custom-review-results/sample-undefined.md"
    write(repo / custom_output, single_pair_bundle_output())
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            "UPDATE review_jobs SET bundle_output_path = ?, runner = ?, runner_model = ? WHERE review_job_id = ?",
            (custom_output, "live-agent", "reviewer-model", review_job_id),
        )
        conn.execute("UPDATE review_pairs SET result_path = ? WHERE review_job_id = ?", (custom_result, review_job_id))
        conn.commit()
    manifest_path = repo / f"kb/reports/bundle-reviews/review-job-{review_job_id}/MANIFEST.json"
    manifest_path.write_text("{not valid json", encoding="utf-8")

    result = run_cli(
        "finalize_review_job",
        "--review-job-id",
        str(review_job_id),
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
    result_text = (repo / custom_result).read_text(encoding="utf-8")
    parsed_frontmatter = frontmatter.parse(result_text)
    assert parsed_frontmatter.ok
    assert parsed_frontmatter.data["review_job_id"] == review_job_id
    assert parsed_frontmatter.data["note_path"] == "kb/notes/sample.md"
    assert parsed_frontmatter.data["gate_path"] == GATE_ONE_PATH
    assert parsed_frontmatter.data["model_partition"] == "test-model"
    assert parsed_frontmatter.data["runner"] == "live-agent"
    assert parsed_frontmatter.data["runner_model"] == "reviewer-model"
    assert parsed_frontmatter.data["runner_effort"] is None
    assert "runner_effort: null\n" in result_text
    assert parsed_frontmatter.data["decision"] == "warn"
    assert parsed_frontmatter.data["reviewed_at"] is not None
    assert frontmatter.strip(result_text) == "Needs a definition for Alpha.\n\n## Result: WARN\n"
    assert not (repo / f"kb/reports/bundle-reviews/review-job-{review_job_id}/undefined-terms.md").exists()
    refreshed_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert refreshed_manifest["bundle_output_path"] == custom_output
    assert refreshed_manifest["pairs"][0]["result_path"] == custom_result
    assert refreshed_manifest["pairs"][0]["status"] == "completed"
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute("SELECT decision, reviewed_at FROM review_pairs").fetchone()
    assert parsed_frontmatter.data["decision"] == row["decision"]
    assert parsed_frontmatter.data["reviewed_at"] == row["reviewed_at"]


def test_finalize_review_job_finalizes_running_job(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    prepared = json.loads(
        run_cli(
            "create_review_jobs",
            "--note",
            "kb/notes/sample.md",
            GATE_ONE,
            "--model",
            "test-model",
            "--grouping",
            "note",
            cwd=repo,
            db_path=db_path,
        ).stdout
    )
    prepared_job = prepared["jobs"][0]
    run_cli(
        "claim_review_job",
        "--review-job-id",
        str(prepared_job["review_job_id"]),
        "--runner",
        "external",
        "--model",
        "test-model",
        cwd=repo,
        db_path=db_path,
    )
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
    assert frontmatter.strip((artifact_dir / "undefined-terms.md").read_text(encoding="utf-8")).strip().endswith("## Result: WARN")
    assert not (artifact_dir / "kb__notes__sample.md :: kb__instructions__review-gates__accessibility__undefined-terms.md").exists()
    manifest = json.loads((artifact_dir / "MANIFEST.json").read_text(encoding="utf-8"))
    assert [pair["status"] for pair in manifest["pairs"]] == ["completed"]
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        job = conn.execute("SELECT status FROM review_jobs").fetchone()
        assert job["status"] == "completed"
        pairs = conn.execute("SELECT gate_path, decision, pair_status FROM review_pairs ORDER BY pair_ordinal").fetchall()
        assert [(row["gate_path"], row["decision"], row["pair_status"]) for row in pairs] == [
            (GATE_ONE_PATH, "warn", "completed"),
        ]
        snapshot_rows = conn.execute(
            """
            SELECT
                rp.reviewed_note_snapshot_id,
                rp.reviewed_gate_snapshot_id,
                ae.accepted_note_snapshot_id,
                ae.accepted_gate_snapshot_id
            FROM review_pairs AS rp
            JOIN acceptance_events AS ae
              ON ae.accepted_review_pair_id = rp.review_pair_id
            ORDER BY rp.pair_ordinal
            """
        ).fetchall()
        assert [
            (
                row["accepted_note_snapshot_id"] == row["reviewed_note_snapshot_id"],
                row["accepted_gate_snapshot_id"] == row["reviewed_gate_snapshot_id"],
            )
            for row in snapshot_rows
        ] == [(True, True)]
        assert conn.execute("SELECT COUNT(*) FROM acceptance_events").fetchone()[0] == 1


def test_run_review_bundles_groups_cross_lens_gates(monkeypatch, tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)

    prompts: list[str] = []

    def fake_run_prompt(**kwargs):
        prompt = kwargs["prompt"]
        prompts.append(prompt)
        blocks = []
        if GATE_ONE_PATH in prompt:
            blocks.append(pair_block("kb/notes/sample.md", GATE_ONE_PATH, "Needs a definition for Alpha.", "WARN"))
        if GATE_TWO_PATH in prompt:
            blocks.append(pair_block("kb/notes/sample.md", GATE_TWO_PATH, "No residue found.", "PASS"))
        return RunnerResult(stdout="\n".join(blocks), stderr="", returncode=0, telemetry=None)

    monkeypatch.setattr(run_review_jobs_lib, "run_prompt", fake_run_prompt)

    result = run_cli(
        "run_review_bundles",
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
    assert "completed 1 1" in result.stdout
    assert "completed 2 1" in result.stdout
    assert len(prompts) == 2
    assert GATE_ONE_PATH in prompts[0]
    assert GATE_TWO_PATH not in prompts[0]
    assert GATE_TWO_PATH in prompts[1]
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        jobs = conn.execute("SELECT status, packing FROM review_jobs ORDER BY review_job_id").fetchall()
        assert [(job["status"], job["packing"]) for job in jobs] == [
            ("completed", "note"),
            ("completed", "note"),
        ]
        decisions = [
            row["decision"]
            for row in conn.execute("SELECT decision FROM review_pairs ORDER BY review_job_id, pair_ordinal")
        ]
        assert decisions == ["warn", "pass"]


def test_run_review_bundles_parse_failure_persists_raw_bundle(monkeypatch, tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)

    def fake_run_prompt(**_kwargs):
        return RunnerResult(stdout="not a pair bundle\n", stderr="", returncode=0, telemetry=None)

    monkeypatch.setattr(run_review_jobs_lib, "run_prompt", fake_run_prompt)

    result = run_cli(
        "run_review_bundles",
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
        job = conn.execute("SELECT status, bundle_output_path, failure_reason FROM review_jobs").fetchone()
        assert job["status"] == "failed"
        assert (repo / job["bundle_output_path"]).read_text(encoding="utf-8") == "not a pair bundle\n"
        assert "missing" in job["failure_reason"] or "pair" in job["failure_reason"]
