"""Batch-granular review job preparation for parent-dispatched execution.

These are the deterministic ends of a review batch. Preparation creates one
queued review job for a note-packed or gate-packed set of pairs and renders the
canonical prompt for a parent-dispatched worker.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from commonplace.review.artifacts import (
    bundle_artifact_dir,
    bundle_output_path_rel,
    prompt_path_rel,
    result_paths_by_pair_id,
    write_manifest,
)
from commonplace.review.freshness import capture_review_inputs
from commonplace.review.finalization import fail_active_review_jobs
from commonplace.review.job_prompt import prepare_note_target
from commonplace.review.protocol.prompt import NoteReviewTarget, render_pairs_prompt
from commonplace.review.review_db import (
    ReviewPairRow,
    connect,
    create_job_with_pairs,
    load_review_pairs_for_job,
)
from commonplace.review.clock import iso_now
from commonplace.review.critique import result_kind_for_gate_path


@dataclass(frozen=True)
class SkippedPair:
    note_path: str
    gate_path: str
    reason: str


@dataclass(frozen=True)
class PreparedBatch:
    review_job_id: int
    targets: list[NoteReviewTarget]
    pairs: list[ReviewPairRow]
    skipped: list[SkippedPair]
    result_paths: dict[int, str]
    prompt_path: str
    bundle_output_path: str
    manifest_path: str


def _targets_for_pairs(
    *,
    repo_root: Path,
    review_job_id: int,
    packing: str,
    pairs: list[tuple[str, str, str]],
    note_texts: dict[str, str] | None = None,
) -> list[NoteReviewTarget]:
    if packing == "note":
        note_paths = {note_path for note_path, _, _ in pairs}
        if len(note_paths) != 1:
            raise ValueError(f"note-packed job requires exactly one note, got: {sorted(note_paths)}")
        note_path = pairs[0][0]
        return [
            prepare_note_target(
                repo_root=repo_root,
                note_path=note_path,
                review_job_id=review_job_id,
                gate_paths=tuple(gate_path for _, gate_path, _ in pairs),
                note_text=note_texts.get(note_path) if note_texts else None,
            )
        ]
    return [
        prepare_note_target(
            repo_root=repo_root,
            note_path=note_path,
            review_job_id=review_job_id,
            gate_paths=(gate_path,),
            note_text=note_texts.get(note_path) if note_texts else None,
        )
        for note_path, gate_path, _ in pairs
    ]


def prepare_grouped_review_job(
    *,
    repo_root: Path,
    db_path: Path,
    pairs: list[tuple[str, str, str]],
    skipped: list[SkippedPair] | None = None,
    packing: str,
    runner: str | None,
    model_partition: str,
    runner_model: str | None = None,
    runner_effort: str | None = None,
    status: str = "queued",
) -> PreparedBatch:
    """Create one review job for already-normalized, applicable pairs."""
    if not pairs:
        raise ValueError("no pairs to prepare")
    for _, gate_path, result_kind in pairs:
        expected_result_kind = result_kind_for_gate_path(gate_path)
        if result_kind != expected_result_kind:
            raise ValueError(
                f"result kind {result_kind!r} does not match gate contract "
                f"{expected_result_kind!r}: {gate_path}"
            )
    result_kinds = {result_kind for _, _, result_kind in pairs}
    if len(result_kinds) != 1:
        raise ValueError("review job cannot mix result kinds")
    created_at = iso_now()
    with connect(db_path) as conn:
        captured_inputs = capture_review_inputs(
            conn,
            repo_root=repo_root,
            pairs=pairs,
        )
        review_job_id = create_job_with_pairs(
            conn,
            model_partition=model_partition,
            runner=runner,
            runner_model=runner_model,
            runner_effort=runner_effort,
            created_at=created_at,
            status=status,
            packing=packing,
            pairs=captured_inputs.pair_requests,
        )
        stored_pairs = load_review_pairs_for_job(conn, review_job_id=review_job_id)
        conn.commit()

    artifact_dir = bundle_artifact_dir(repo_root, review_job_id)
    bundle_output_path = bundle_output_path_rel(review_job_id)
    result_paths = result_paths_by_pair_id(
        review_job_id=review_job_id,
        packing=packing,
        pairs=stored_pairs,
    )
    prompt_path = prompt_path_rel(review_job_id)
    # Prompt rendering and every artifact write must fail the queued job:
    # a job left queued without its prompt on disk is undispatchable and
    # nothing else would ever clean it up.
    try:
        targets = _targets_for_pairs(
            repo_root=repo_root,
            review_job_id=review_job_id,
            packing=packing,
            pairs=pairs,
            note_texts=captured_inputs.note_texts,
        )
        prompt = render_pairs_prompt(
            notes=targets,
            gate_texts=captured_inputs.gate_texts,
            result_kind=next(iter(result_kinds)),
            output_mode="file",
            bundle_output_path=bundle_output_path,
        )
        artifact_dir.mkdir(parents=True, exist_ok=True)
        (repo_root / prompt_path).write_text(prompt, encoding="utf-8")
        manifest_path = write_manifest(
            repo_root=repo_root,
            artifact_dir=artifact_dir,
            review_job_id=review_job_id,
            job_status=status,
            packing=packing,
            prompt_path=prompt_path,
            bundle_output_path=bundle_output_path,
            pairs=stored_pairs,
            skipped=skipped,
        )
    except (ValueError, OSError) as exc:
        fail_active_review_jobs(
            db_path=db_path,
            review_job_ids=[review_job_id],
            failure_reason=str(exc),
        )
        raise

    return PreparedBatch(
        review_job_id=review_job_id,
        targets=targets,
        pairs=stored_pairs,
        skipped=skipped or [],
        result_paths=result_paths,
        prompt_path=prompt_path,
        bundle_output_path=bundle_output_path,
        manifest_path=manifest_path,
    )
