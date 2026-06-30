"""Single-gate multi-note review: the share-gate packing of the pair executor.

Pure logic lives here; commonplace.cli.review.run_gate_sweep is the thin CLI
wrapper.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.review.batch import prepare_grouped_review_job
from commonplace.review.executor import prepare_note_target
from commonplace.review.paths import normalize_gate_path
from commonplace.review.protocol.prompt import NoteReviewTarget, render_pairs_prompt
from commonplace.review.review_db import (
    connect,
    load_review_pairs_for_job,
)
from commonplace.review.review_model import normalize_model_partition
from commonplace.review.review_target_selector import select_stale_gates
from commonplace.review.run_review_jobs import run_review_jobs


def chunked(items: list[str], size: int) -> list[list[str]]:
    return [items[index : index + size] for index in range(0, len(items), size)]


@dataclass(frozen=True)
class PreparedGateBatch:
    targets: list[NoteReviewTarget]
    gate_texts: dict[str, str]


@dataclass(frozen=True)
class GateSweepOutcome:
    exit_code: int
    stdout: str = ""
    stderr: str = ""


def _append_line(text: str, line: str = "") -> str:
    return text + line + "\n"


def batch_pair_status_counts(db_path: Path, review_job_ids: list[int]) -> tuple[int, int]:
    completed = 0
    missing = 0
    with connect(db_path) as conn:
        for review_job_id in review_job_ids:
            for pair in load_review_pairs_for_job(conn, review_job_id=review_job_id):
                if pair.pair_status == "completed":
                    completed += 1
                elif pair.pair_status == "missing":
                    missing += 1
    return completed, missing


def prepare_batch_targets(
    *,
    repo_root: Path,
    note_paths: list[str],
    gate_path: str,
) -> PreparedGateBatch:
    """Build dry-run targets without creating review jobs."""
    gate_text = frontmatter.strip((repo_root / gate_path).read_text(encoding="utf-8")).lstrip("\n")
    return PreparedGateBatch(
        targets=[
            prepare_note_target(
                repo_root=repo_root,
                note_path=note_path,
                review_job_id=0,
                gate_paths=(gate_path,),
            )
            for note_path in note_paths
        ],
        gate_texts={gate_path: gate_text},
    )


def run_gate_sweep(
    *,
    repo_root: Path,
    db_path: Path,
    gate_path: str,
    runner: str,
    model: str,
    note_paths: list[str] | None,
    current_only: bool,
    batch_size: int,
    dry_run: bool,
    missing_any_review: bool = False,
) -> GateSweepOutcome:
    """Run one gate across many notes in batched runner calls.

    Returns a process exit code. Raises ValueError on input/precondition
    errors so the caller can translate them to argparse-style failures.
    """
    runner_model = model
    model = normalize_model_partition(model)
    raw_gate = gate_path
    gate_path = normalize_gate_path(repo_root, raw_gate)
    gate_abs = repo_root / gate_path
    if not gate_abs.is_file():
        raise ValueError(f"gate not found: {gate_path}")

    stale_records = select_stale_gates(
        repo_root,
        model=None if missing_any_review else model,
        gate_ids=[gate_path],
        note_filter=note_paths,
        current_only=current_only,
        include_diff=False,
        db_path=db_path,
    )

    sweep_note_paths = [record.note_path for record in stale_records]
    if not sweep_note_paths:
        return GateSweepOutcome(exit_code=0, stdout="Reviewed: 0 notes\n")

    batches = chunked(sweep_note_paths, batch_size)
    stdout = ""
    stderr = f"Selected: {len(sweep_note_paths)} notes across {len(batches)} batches\n"

    reviewed = 0
    failed = 0
    missing = 0
    for batch_index, batch_note_paths in enumerate(batches, start=1):
        if dry_run:
            prepared_batch = prepare_batch_targets(
                repo_root=repo_root,
                note_paths=batch_note_paths,
                gate_path=gate_path,
            )
            targets = prepared_batch.targets
            review_job_ids = sorted({target.review_job_id for target in targets})
        else:
            prepared = prepare_grouped_review_job(
                repo_root=repo_root,
                db_path=db_path,
                pairs=[(note_path, gate_path) for note_path in batch_note_paths],
                packing="gate",
                runner=None,
                model_partition=model,
            )
            targets = prepared.targets
            review_job_ids = [prepared.review_job_id]
        batch_label = f"Batch {batch_index}/{len(batches)}"
        stderr = _append_line(stderr, f"{batch_label}: launching {runner} for {len(targets)} notes")
        for target in targets:
            stderr = _append_line(stderr, f"  - {target.note_path} (review job id: {target.review_job_id})")

        if dry_run:
            prompt = render_pairs_prompt(notes=targets, gate_texts=prepared_batch.gate_texts)
            if batch_index > 1:
                stdout = _append_line(stdout)
                stdout = _append_line(stdout, f"=== BATCH {batch_index}/{len(batches)} ===")
            stdout = _append_line(stdout, prompt)
            continue

        payload, status = run_review_jobs(
            repo_root=repo_root,
            db_path=db_path,
            runner=runner,
            model=runner_model,
            review_job_id=review_job_ids[0],
        )
        if status == 130:
            stderr = _append_line(stderr, "gate sweep interrupted")
            return GateSweepOutcome(exit_code=130, stdout=stdout, stderr=stderr)
        if payload.get("usage_exhausted"):
            stderr = _append_line(stderr, "error: runner reported usage exhausted; aborting sweep.")
            return GateSweepOutcome(exit_code=1, stdout=stdout, stderr=stderr)

        completed_count, missing_count = batch_pair_status_counts(db_path, review_job_ids)
        reviewed += completed_count
        missing += missing_count
        runner_returncode = 0
        for job in payload.get("jobs", []):
            if not isinstance(job, dict):
                continue
            if job.get("status") == "failed":
                failed += 1
                stderr = _append_line(
                    stderr,
                    f"  FAILED job {job['review_job_id']}: {job.get('failure_reason')}",
                )
            if isinstance(job.get("runner_returncode"), int):
                runner_returncode = int(job["runner_returncode"])
        stdout = _append_line(stdout, f"{batch_label}: reviewed {completed_count} notes")
        if missing_count:
            stderr = _append_line(stderr, f"{batch_label}: missing {missing_count} notes")
        if runner_returncode != 0:
            return GateSweepOutcome(exit_code=runner_returncode, stdout=stdout, stderr=stderr)

    if not dry_run:
        stdout = _append_line(stdout, f"Reviewed: {reviewed} notes")
        if missing:
            stderr = _append_line(stderr, f"Missing:  {missing} notes")
        if failed:
            stderr = _append_line(stderr, f"Failed:   {failed} job(s)")
            return GateSweepOutcome(exit_code=1, stdout=stdout, stderr=stderr)
    return GateSweepOutcome(exit_code=0, stdout=stdout, stderr=stderr)
