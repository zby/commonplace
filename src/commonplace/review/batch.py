"""Batch-granular prepare/ingest for harness-orchestrated review execution.

These are the deterministic ends of a review batch when something other than
the subprocess runner executes it. prepare creates one review invocation for a
note-packed or gate-packed set of pairs and renders the canonical prompt;
ingest parses pair output and finalizes pair records with the executor's
salvage policy.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.review.artifacts import write_manifest, write_pair_result_files
from commonplace.review.executor import (
    RunPairs,
    bundle_artifact_dir,
    fail_running_review_runs,
    finalize_run_records_from_parsed,
    prepare_note_target,
)
from commonplace.review.paths import GATES_ROOT
from commonplace.review.protocol.parser import parse_pair_bundle
from commonplace.review.protocol.prompt import NoteReviewTarget, render_pairs_prompt
from commonplace.review.resolve_gates import applicable_gate_ids_for_note
from commonplace.review.review_db import (
    ReviewPairRequest,
    ReviewPairRow,
    connect,
    create_run_with_pairs,
    load_review_pairs_for_run,
    load_review_run,
    mark_missing_pairs,
)
from commonplace.review.review_metadata import committed_file_provenance, iso_now, review_note_provenance


PAIR_ARG_SEPARATOR = "::"


@dataclass(frozen=True)
class SkippedPair:
    note_path: str
    gate_id: str
    reason: str


@dataclass(frozen=True)
class PreparedBatch:
    review_run_id: int
    targets: list[NoteReviewTarget]
    pairs: list[ReviewPairRow]
    skipped: list[SkippedPair]
    prompt_path: str
    bundle_output_path: str
    manifest_path: str


def parse_pair_args(raw_pairs: list[str]) -> list[tuple[str, str]]:
    """Parse `note-path::gate-id` arguments into (note_path, gate_id) pairs."""
    pairs: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for raw in raw_pairs:
        note_path, separator, gate_id = raw.partition(PAIR_ARG_SEPARATOR)
        note_path = note_path.strip()
        gate_id = gate_id.strip().removesuffix(".md")
        if not separator or not note_path or not gate_id:
            raise ValueError(f"malformed pair (expected note-path::gate-id): {raw}")
        pair = (note_path, gate_id)
        if pair in seen:
            raise ValueError(f"duplicate pair: {raw}")
        seen.add(pair)
        pairs.append(pair)
    return pairs


def _packing_for_pairs(pairs: list[tuple[str, str]]) -> str:
    note_paths = {note_path for note_path, _ in pairs}
    gate_ids = {gate_id for _, gate_id in pairs}
    if len(note_paths) == 1:
        return "note"
    if len(gate_ids) == 1:
        return "gate"
    raise ValueError("review batch pairs must share one note or one gate")


def _targets_for_pairs(
    *,
    repo_root: Path,
    review_run_id: int,
    packing: str,
    pairs: list[tuple[str, str]],
) -> list[NoteReviewTarget]:
    if packing == "note":
        note_path = pairs[0][0]
        return [
            prepare_note_target(
                repo_root=repo_root,
                note_path=note_path,
                review_run_id=review_run_id,
                gate_ids=tuple(gate_id for _, gate_id in pairs),
            )
        ]
    return [
        prepare_note_target(
            repo_root=repo_root,
            note_path=note_path,
            review_run_id=review_run_id,
            gate_ids=(gate_id,),
        )
        for note_path, gate_id in pairs
    ]


def _applicable_pairs(repo_root: Path, pairs: list[tuple[str, str]]) -> tuple[list[tuple[str, str]], list[SkippedPair]]:
    gates_dir = repo_root / GATES_ROOT
    grouped: dict[str, list[str]] = {}
    for note_path, gate_id in pairs:
        grouped.setdefault(note_path, []).append(gate_id)

    applicable_by_note: dict[str, set[str]] = {}
    skipped: list[SkippedPair] = []
    for note_path, gate_ids in grouped.items():
        note_abs = repo_root / note_path
        if not note_abs.is_file():
            raise ValueError(f"note not found: {note_path}")
        applicable = set(applicable_gate_ids_for_note(note_abs, gate_ids, gates_dir))
        applicable_by_note[note_path] = applicable
        for gate_id in gate_ids:
            if gate_id not in applicable:
                skipped.append(SkippedPair(note_path=note_path, gate_id=gate_id, reason="not applicable"))

    applicable_pairs = [(note_path, gate_id) for note_path, gate_id in pairs if gate_id in applicable_by_note[note_path]]
    return applicable_pairs, skipped


def prepare_review_batch(
    *,
    repo_root: Path,
    db_path: Path,
    pairs: list[tuple[str, str]],
    runner: str,
    model_id: str,
) -> PreparedBatch:
    """Create one review run for the given note-packed or gate-packed pairs."""
    applicable_pairs, skipped = _applicable_pairs(repo_root, pairs)
    if not applicable_pairs:
        raise ValueError("no applicable pairs to prepare")
    packing = _packing_for_pairs(applicable_pairs)

    gates_dir = repo_root / GATES_ROOT
    gate_shas: dict[str, str] = {}
    gate_texts: dict[str, str] = {}
    for gate_id in sorted({gate_id for _, gate_id in applicable_pairs}):
        gate_abs = gates_dir / f"{gate_id}.md"
        if not gate_abs.is_file():
            raise ValueError(f"gate not found: {gate_id}")
        gate_shas[gate_id], _ = committed_file_provenance(repo_root, gate_abs, kind="gate")
        gate_texts[gate_id] = frontmatter.strip(gate_abs.read_text(encoding="utf-8")).lstrip("\n")

    note_provenance: dict[str, tuple[str, str | None]] = {}
    for note_path in sorted({note_path for note_path, _ in applicable_pairs}):
        note_provenance[note_path] = review_note_provenance(repo_root, Path(note_path))

    started_at = iso_now()
    pair_requests = [
        ReviewPairRequest(
            note_path=note_path,
            gate_id=gate_id,
            gate_sha=gate_shas[gate_id],
            reviewed_note_sha=note_provenance[note_path][0],
            reviewed_note_commit=note_provenance[note_path][1],
            pair_ordinal=ordinal,
        )
        for ordinal, (note_path, gate_id) in enumerate(applicable_pairs)
    ]
    with connect(db_path) as conn:
        review_run_id = create_run_with_pairs(
            conn,
            model_id=model_id,
            runner=runner,
            started_at=started_at,
            packing=packing,
            pairs=pair_requests,
        )
        stored_pairs = load_review_pairs_for_run(conn, review_run_id=review_run_id)
        conn.commit()

    targets = _targets_for_pairs(
        repo_root=repo_root,
        review_run_id=review_run_id,
        packing=packing,
        pairs=applicable_pairs,
    )
    artifact_dir = bundle_artifact_dir(repo_root, review_run_id)
    bundle_output_path = (artifact_dir / "bundle-output.md").relative_to(repo_root).as_posix()
    try:
        prompt = render_pairs_prompt(
            notes=targets,
            gate_texts=gate_texts,
            output_mode="file",
            bundle_output_path=bundle_output_path,
        )
    except ValueError as exc:
        fail_running_review_runs(
            db_path=db_path,
            review_run_ids=[review_run_id],
            failure_reason=str(exc),
        )
        raise

    artifact_dir.mkdir(parents=True, exist_ok=True)
    prompt_abs = artifact_dir / "prompt.md"
    prompt_abs.write_text(prompt, encoding="utf-8")
    prompt_path = prompt_abs.relative_to(repo_root).as_posix()
    manifest_path = write_manifest(
        repo_root=repo_root,
        artifact_dir=artifact_dir,
        review_run_id=review_run_id,
        packing=packing,
        prompt_path=prompt_path,
        bundle_output_path=bundle_output_path,
        pairs=stored_pairs,
        skipped=skipped,
    )

    return PreparedBatch(
        review_run_id=review_run_id,
        targets=targets,
        pairs=stored_pairs,
        skipped=skipped,
        prompt_path=prompt_path,
        bundle_output_path=bundle_output_path,
        manifest_path=manifest_path,
    )


def ingest_batch_output(
    *,
    repo_root: Path,
    db_path: Path,
    review_run_id: int,
    raw_bundle_markdown: str,
) -> tuple[list[int], list[tuple[int, str]]]:
    """Parse a batch's pair output and finalize its run with pair salvage."""
    with connect(db_path) as conn:
        review_run = load_review_run(conn, review_run_id=review_run_id)
        if review_run is None:
            raise ValueError(f"review run not found: {review_run_id}")
        if review_run.status != "running":
            raise ValueError(f"review run is not ingestible: {review_run_id} ({review_run.status})")
        stored_pairs = load_review_pairs_for_run(conn, review_run_id=review_run_id)

    expected_pairs = [(pair.note_path, pair.gate_id) for pair in stored_pairs]
    try:
        parsed = parse_pair_bundle(raw_bundle_markdown, expected_pairs=expected_pairs)
    except ValueError as exc:
        with connect(db_path) as conn:
            mark_missing_pairs(conn, review_run_id=review_run_id)
            conn.commit()
        fail_running_review_runs(
            db_path=db_path,
            review_run_ids=[review_run_id],
            failure_reason=str(exc),
            raw_bundle_markdown=raw_bundle_markdown,
        )
        raise

    completed, failed = finalize_run_records_from_parsed(
        db_path=db_path,
        run_pairs=[RunPairs(review_run_id=review_run_id, pairs=tuple(expected_pairs))],
        parsed=parsed,
        raw_output=raw_bundle_markdown,
    )

    artifact_dir = bundle_artifact_dir(repo_root, review_run_id)
    artifact_dir.mkdir(parents=True, exist_ok=True)
    bundle_output_path = (artifact_dir / "bundle-output.md").relative_to(repo_root).as_posix()
    prompt_path = (artifact_dir / "prompt.md").relative_to(repo_root).as_posix()
    (artifact_dir / "bundle-output.md").write_text(raw_bundle_markdown, encoding="utf-8")
    with connect(db_path) as conn:
        updated_run = load_review_run(conn, review_run_id=review_run_id)
        updated_pairs = load_review_pairs_for_run(conn, review_run_id=review_run_id)
    write_pair_result_files(
        artifact_dir=artifact_dir,
        packing=review_run.packing,
        pairs=[(pair.note_path, pair.gate_id) for pair in updated_pairs],
        canonical_texts=parsed.canonical_texts,
    )
    write_manifest(
        repo_root=repo_root,
        artifact_dir=artifact_dir,
        review_run_id=review_run_id,
        packing=review_run.packing,
        prompt_path=prompt_path,
        bundle_output_path=bundle_output_path,
        pairs=updated_pairs,
        failure_reason=updated_run.failure_reason if updated_run is not None else None,
    )
    return completed, failed
