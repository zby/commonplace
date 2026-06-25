"""Single-gate multi-note review: the share-gate packing of the pair executor.

Pure logic lives here; commonplace.cli.review.run_gate_sweep is the thin CLI
wrapper.
"""

from __future__ import annotations

from dataclasses import dataclass
import sys
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.review.executor import (
    UsageExhausted,
    bundle_artifact_dir,
    execute_batch,
    prepare_note_target,
)
from commonplace.review.freshness import capture_review_inputs
from commonplace.review.paths import normalize_gate_path
from commonplace.review.protocol.prompt import NoteReviewTarget, render_pairs_prompt
from commonplace.review.review_db import (
    connect,
    create_run_with_pairs,
    load_review_pairs_for_run,
)
from commonplace.review.review_metadata import iso_now
from commonplace.review.review_model import normalize_model_partition
from commonplace.review.review_target_selector import select_stale_gates


def chunked(items: list[str], size: int) -> list[list[str]]:
    return [items[index : index + size] for index in range(0, len(items), size)]


@dataclass(frozen=True)
class PreparedGateBatch:
    targets: list[NoteReviewTarget]
    gate_texts: dict[str, str]


def batch_pair_status_counts(db_path: Path, review_run_ids: list[int]) -> tuple[int, int]:
    completed = 0
    missing = 0
    with connect(db_path) as conn:
        for review_run_id in review_run_ids:
            for pair in load_review_pairs_for_run(conn, review_run_id=review_run_id):
                if pair.pair_status == "completed":
                    completed += 1
                elif pair.pair_status == "missing":
                    missing += 1
    return completed, missing


def prepare_batch_targets(
    *,
    repo_root: Path,
    db_path: Path | None,
    note_paths: list[str],
    gate_path: str,
    runner: str,
    model_partition: str,
) -> PreparedGateBatch:
    """Create one single-gate review run for this prompt batch.

    With db_path=None (dry run) no runs are created and ordinals stand in for
    run ids.
    """
    if db_path is None:
        gate_text = frontmatter.strip((repo_root / gate_path).read_text(encoding="utf-8")).lstrip("\n")
        return PreparedGateBatch(
            targets=[
                prepare_note_target(
                    repo_root=repo_root,
                    note_path=note_path,
                    review_run_id=0,
                    gate_paths=(gate_path,),
                )
                for note_path in note_paths
            ],
            gate_texts={gate_path: gate_text},
        )

    targets: list[NoteReviewTarget] = []
    started_at = iso_now()
    with connect(db_path) as conn:
        captured_inputs = capture_review_inputs(
            conn,
            repo_root=repo_root,
            pairs=[(note_path, gate_path) for note_path in note_paths],
        )
        review_run_id = create_run_with_pairs(
            conn,
            model_partition=model_partition,
            runner=runner,
            started_at=started_at,
            packing="gate",
            pairs=captured_inputs.pair_requests,
        )
        bundle_artifact_dir(repo_root, review_run_id).mkdir(parents=True, exist_ok=True)
        for note_path in note_paths:
            targets.append(
                prepare_note_target(
                    repo_root=repo_root,
                    note_path=note_path,
                    review_run_id=review_run_id,
                    gate_paths=(gate_path,),
                    note_text=captured_inputs.note_texts[note_path],
                )
            )
        conn.commit()
    return PreparedGateBatch(targets=targets, gate_texts=captured_inputs.gate_texts)


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
) -> int:
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
        model=model,
        gate_ids=[gate_path],
        note_filter=note_paths,
        current_only=current_only,
        include_diff=False,
        db_path=db_path,
    )

    sweep_note_paths = [record.note_path for record in stale_records]
    if not sweep_note_paths:
        print("Reviewed: 0 notes")
        return 0

    batches = chunked(sweep_note_paths, batch_size)
    print(f"Selected: {len(sweep_note_paths)} notes across {len(batches)} batches", file=sys.stderr)

    reviewed = 0
    failed = 0
    missing = 0
    for batch_index, batch_note_paths in enumerate(batches, start=1):
        prepared_batch = prepare_batch_targets(
            repo_root=repo_root,
            db_path=None if dry_run else db_path,
            note_paths=batch_note_paths,
            gate_path=gate_path,
            runner=runner,
            model_partition=model,
        )
        targets = prepared_batch.targets
        batch_label = f"Batch {batch_index}/{len(batches)}"
        print(f"{batch_label}: launching {runner} for {len(targets)} notes", file=sys.stderr)
        for target in targets:
            print(f"  - {target.note_path} (review run id: {target.review_run_id})", file=sys.stderr)
        review_run_ids = sorted({target.review_run_id for target in targets})

        if dry_run:
            prompt = render_pairs_prompt(notes=targets, gate_texts=prepared_batch.gate_texts)
            if batch_index > 1:
                print()
                print(f"=== BATCH {batch_index}/{len(batches)} ===")
            print(prompt)
            continue

        try:
            outcome = execute_batch(
                repo_root=repo_root,
                db_path=db_path,
                targets=targets,
                gate_texts=prepared_batch.gate_texts,
                runner=runner,
                runner_model=runner_model,
                model_partition=model,
            )
        except KeyboardInterrupt:
            print("gate sweep interrupted", file=sys.stderr)
            return 130
        except UsageExhausted:
            print("error: runner reported usage exhausted; aborting sweep.", file=sys.stderr)
            return 1

        completed_count, missing_count = batch_pair_status_counts(db_path, review_run_ids)
        reviewed += completed_count
        missing += missing_count
        failed += len(outcome.failed)
        for review_run_id, reason in outcome.failed:
            print(f"  FAILED run {review_run_id}: {reason}", file=sys.stderr)
        print(f"{batch_label}: reviewed {completed_count} notes")
        if missing_count:
            print(f"{batch_label}: missing {missing_count} notes", file=sys.stderr)
        if outcome.runner_returncode != 0:
            return outcome.runner_returncode

    if not dry_run:
        print(f"Reviewed: {reviewed} notes")
        if missing:
            print(f"Missing:  {missing} notes", file=sys.stderr)
        if failed:
            print(f"Failed:   {failed} run(s)", file=sys.stderr)
            return 1
    return 0
