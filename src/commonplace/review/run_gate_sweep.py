"""Single-gate multi-note review: the share-gate packing of the pair executor.

Pure logic lives here; commonplace.cli.review.run_gate_sweep is the thin CLI
wrapper.
"""

from __future__ import annotations

import sys
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.review.executor import (
    UsageExhausted,
    bundle_artifact_dir,
    execute_batch,
    prepare_note_target,
)
from commonplace.review.paths import GATES_ROOT
from commonplace.review.protocol.prompt import NoteReviewTarget, render_pairs_prompt
from commonplace.review.review_db import ReviewPairRequest, connect, create_run_with_pairs
from commonplace.review.review_metadata import committed_file_provenance, iso_now, review_note_provenance
from commonplace.review.review_model import normalize_model_id
from commonplace.review.review_target_selector import select_stale_gates


def chunked(items: list[str], size: int) -> list[list[str]]:
    return [items[index : index + size] for index in range(0, len(items), size)]


def prepare_batch_targets(
    *,
    repo_root: Path,
    db_path: Path | None,
    note_paths: list[str],
    gate_id: str,
    gate_sha: str,
    runner: str,
    model_id: str,
) -> list[NoteReviewTarget]:
    """Create one single-gate review run for this prompt batch.

    With db_path=None (dry run) no runs are created and ordinals stand in for
    run ids.
    """
    if db_path is None:
        return [
            prepare_note_target(
                repo_root=repo_root,
                note_path=note_path,
                review_run_id=0,
                gate_ids=(gate_id,),
            )
            for note_path in note_paths
        ]

    targets: list[NoteReviewTarget] = []
    started_at = iso_now()
    with connect(db_path) as conn:
        pair_requests: list[ReviewPairRequest] = []
        for ordinal, note_path in enumerate(note_paths):
            note_sha, note_commit = review_note_provenance(repo_root, Path(note_path))
            pair_requests.append(
                ReviewPairRequest(
                    note_path=note_path,
                    gate_id=gate_id,
                    gate_sha=gate_sha,
                    reviewed_note_sha=note_sha,
                    reviewed_note_commit=note_commit,
                    pair_ordinal=ordinal,
                )
            )
        review_run_id = create_run_with_pairs(
            conn,
            model_id=model_id,
            runner=runner,
            started_at=started_at,
            packing="gate",
            pairs=pair_requests,
        )
        bundle_artifact_dir(repo_root, review_run_id).mkdir(parents=True, exist_ok=True)
        for note_path in note_paths:
            targets.append(
                prepare_note_target(
                    repo_root=repo_root,
                    note_path=note_path,
                    review_run_id=review_run_id,
                    gate_ids=(gate_id,),
                )
            )
        conn.commit()
    return targets


def run_gate_sweep(
    *,
    repo_root: Path,
    db_path: Path,
    gate_id: str,
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
    model = normalize_model_id(model)
    gate_id = gate_id.removesuffix(".md")
    gate_abs = repo_root / GATES_ROOT / f"{gate_id}.md"
    if not gate_abs.is_file():
        raise ValueError(f"gate not found: {gate_id}")
    gate_text = frontmatter.strip(gate_abs.read_text(encoding="utf-8")).lstrip("\n")
    gate_sha, _ = committed_file_provenance(repo_root, gate_abs, kind="gate")

    stale_records = select_stale_gates(
        repo_root,
        model=model,
        gate_ids=[gate_id],
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
    for batch_index, batch_note_paths in enumerate(batches, start=1):
        targets = prepare_batch_targets(
            repo_root=repo_root,
            db_path=None if dry_run else db_path,
            note_paths=batch_note_paths,
            gate_id=gate_id,
            gate_sha=gate_sha,
            runner=runner,
            model_id=model,
        )
        batch_label = f"Batch {batch_index}/{len(batches)}"
        print(f"{batch_label}: launching {runner} for {len(targets)} notes", file=sys.stderr)
        for target in targets:
            print(f"  - {target.note_path} (review run id: {target.review_run_id})", file=sys.stderr)

        if dry_run:
            prompt = render_pairs_prompt(notes=targets, gate_texts={gate_id: gate_text})
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
                gate_texts={gate_id: gate_text},
                runner=runner,
                runner_model=runner_model,
                model_id=model,
            )
        except KeyboardInterrupt:
            print("gate sweep interrupted", file=sys.stderr)
            return 130
        except UsageExhausted:
            print("error: runner reported usage exhausted; aborting sweep.", file=sys.stderr)
            return 1

        if outcome.runner_returncode != 0:
            return outcome.runner_returncode

        reviewed += len(batch_note_paths) if outcome.completed else 0
        failed += len(outcome.failed)
        for review_run_id, reason in outcome.failed:
            print(f"  FAILED run {review_run_id}: {reason}", file=sys.stderr)
        print(f"{batch_label}: reviewed {len(batch_note_paths) if outcome.completed else 0} notes")

    if not dry_run:
        print(f"Reviewed: {reviewed} notes")
        if failed:
            print(f"Failed:   {failed} notes", file=sys.stderr)
            return 1
    return 0
