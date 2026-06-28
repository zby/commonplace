"""Run note-local review bundles through a subprocess runner."""

from __future__ import annotations

import sys
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.review.executor import execute_batch, prepare_note_target
from commonplace.review.freshness import capture_review_inputs
from commonplace.review.gate_packing import GateBundleGroup, group_requested_gates_by_bundle
from commonplace.review.protocol.prompt import render_pairs_prompt
from commonplace.review.review_db import connect, create_run_with_pairs, ensure_db
from commonplace.review.clock import iso_now
from commonplace.review.review_model import normalize_model_partition


def _dry_run_prompt(
    *,
    repo_root: Path,
    note_path: str,
    group: GateBundleGroup,
) -> str:
    target = prepare_note_target(
        repo_root=repo_root,
        note_path=note_path,
        review_run_id=0,
        gate_paths=tuple(group.gate_paths),
    )
    gate_texts = {
        gate_path: frontmatter.strip((repo_root / gate_path).read_text(encoding="utf-8")).lstrip("\n")
        for gate_path in group.gate_paths
    }
    return render_pairs_prompt(notes=[target], gate_texts=gate_texts)


def _run_group(
    *,
    repo_root: Path,
    db_path: Path,
    note_path: str,
    group: GateBundleGroup,
    runner: str,
    runner_model: str,
    model_partition: str,
    dry_run: bool,
) -> int:
    if dry_run:
        print(f"=== Bundle: {group.bundle} ===")
        print(_dry_run_prompt(repo_root=repo_root, note_path=note_path, group=group))
        print()
        return 0

    with connect(db_path) as conn:
        captured_inputs = capture_review_inputs(
            conn,
            repo_root=repo_root,
            pairs=[(note_path, gate_path) for gate_path in group.gate_paths],
        )
        started_at = iso_now()
        review_run_id = create_run_with_pairs(
            conn,
            model_partition=model_partition,
            runner=runner,
            created_at=started_at,
            started_at=started_at,
            status="running",
            packing="note",
            pairs=captured_inputs.pair_requests,
        )
        conn.commit()

    target = prepare_note_target(
        repo_root=repo_root,
        note_path=note_path,
        review_run_id=review_run_id,
        gate_paths=tuple(group.gate_paths),
        note_text=captured_inputs.note_texts[note_path],
    )
    outcome = execute_batch(
        repo_root=repo_root,
        db_path=db_path,
        targets=[target],
        gate_texts=captured_inputs.gate_texts,
        runner=runner,
        runner_model=runner_model,
        model_partition=model_partition,
    )

    if outcome.runner_returncode != 0:
        return outcome.runner_returncode
    if outcome.failed:
        for _, reason in outcome.failed:
            print(reason, file=sys.stderr)
        return 1
    print(f"completed {review_run_id} {len(group.gate_paths)}")
    return 0


def run_bundles(
    *,
    repo_root: Path,
    db_path: Path,
    note_path: str,
    gate_or_bundle: list[str],
    runner: str,
    model: str,
    dry_run: bool,
) -> int:
    """Run requested gates as one subprocess call per bundle/lens."""
    runner_model = model
    model_partition = normalize_model_partition(model)
    groups = group_requested_gates_by_bundle(
        repo_root=repo_root,
        note_path=note_path,
        gate_or_bundle=gate_or_bundle,
    )

    if not dry_run:
        ensure_db(db_path)

    for group in groups:
        status = _run_group(
            repo_root=repo_root,
            db_path=db_path,
            note_path=note_path,
            group=group,
            runner=runner,
            runner_model=runner_model,
            model_partition=model_partition,
            dry_run=dry_run,
        )
        if status != 0:
            return status
    return 0
