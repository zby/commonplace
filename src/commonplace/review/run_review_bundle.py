"""Multi-gate single-note review: the share-note packing of the pair executor.

Pure logic lives here; commonplace.cli.review.run_review_bundle is the thin
CLI wrapper.
"""

from __future__ import annotations

import sys
from pathlib import Path

from commonplace.review.executor import execute_batch, prepare_note_target
from commonplace.review.freshness import capture_review_inputs
from commonplace.review.protocol.prompt import OutputMode, render_pairs_prompt
from commonplace.review.review_db import connect, create_run_with_pairs, ensure_db
from commonplace.review.review_metadata import resolve_review_target
from commonplace.review.review_model import normalize_model_partition


def build_review_run_prompt(
    *,
    repo_root: Path,
    note_path: str,
    gate_paths: list[str],
    gate_texts: dict[str, str],
    review_run_id: int,
    output_mode: OutputMode = "stdout",
    bundle_output_path: str | None = None,
    note_text: str | None = None,
) -> str:
    target = prepare_note_target(
        repo_root=repo_root,
        note_path=note_path,
        review_run_id=review_run_id,
        gate_paths=tuple(gate_paths),
        note_text=note_text,
    )
    return render_pairs_prompt(
        notes=[target],
        gate_texts=gate_texts,
        output_mode=output_mode,
        bundle_output_path=bundle_output_path,
    )


def run_bundle(
    *,
    repo_root: Path,
    db_path: Path,
    note_path: str,
    gate_or_bundle: list[str],
    runner: str,
    model: str,
    dry_run: bool,
) -> int:
    """Run one review bundle end-to-end. Returns a process exit code.

    Callers are responsible for validating note_path and model before calling;
    this function assumes both are well-formed.
    """
    runner_model = model
    model = normalize_model_partition(model)

    _note_sha, _note_commit, started_at, run_gates, gate_texts = resolve_review_target(
        repo_root, note_path, gate_or_bundle,
    )
    gate_paths = [g[0] for g in run_gates]

    if dry_run:
        dry_run_prompt = build_review_run_prompt(
            repo_root=repo_root,
            note_path=note_path,
            gate_paths=gate_paths,
            gate_texts=gate_texts,
            review_run_id=0,
        )
        print(dry_run_prompt)
        return 0

    ensure_db(repo_root, db_path)

    with connect(db_path) as conn:
        captured_inputs = capture_review_inputs(
            conn,
            repo_root=repo_root,
            pairs=[(note_path, gate_path) for gate_path in gate_paths],
        )
        review_run_id = create_run_with_pairs(
            conn,
            model_partition=model,
            runner=runner,
            started_at=started_at,
            packing="note",
            pairs=captured_inputs.pair_requests,
        )
        conn.commit()

    target = prepare_note_target(
        repo_root=repo_root,
        note_path=note_path,
        review_run_id=review_run_id,
        gate_paths=tuple(gate_paths),
        note_text=captured_inputs.note_texts[note_path],
    )
    outcome = execute_batch(
        repo_root=repo_root,
        db_path=db_path,
        targets=[target],
        gate_texts=captured_inputs.gate_texts,
        runner=runner,
        runner_model=runner_model,
        model_partition=model,
    )

    if outcome.runner_returncode != 0:
        return outcome.runner_returncode
    if outcome.failed:
        for _, reason in outcome.failed:
            print(reason, file=sys.stderr)
        return 1
    print(f"completed {review_run_id} {len(gate_paths)}")
    return 0
