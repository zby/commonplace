"""Batch-granular prepare/ingest for harness-orchestrated review execution.

These are the deterministic ends of a review batch when something other than
the subprocess runner executes it — a live agent, or an external orchestrator
(e.g. a harness workflow) fanning batches out to sub-agents. prepare creates
the review runs for an arbitrary set of (note, gate) pairs and renders one
canonical prompt; ingest parses the pair output and finalizes with the same
salvage policy as the executor.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.review.executor import (
    BUNDLE_ARTIFACTS_ROOT,
    bundle_artifact_dir,
    fail_running_review_runs,
    finalize_runs_from_parsed,
    prepare_note_target,
    RunPairs,
)
from commonplace.review.paths import GATES_ROOT
from commonplace.review.protocol.parser import parse_pair_bundle
from commonplace.review.protocol.prompt import NoteReviewTarget, render_pairs_prompt
from commonplace.review.resolve_gates import applicable_gate_ids_for_note
from commonplace.review.review_db import connect, create_run, load_review_run, load_review_run_gates
from commonplace.review.review_metadata import committed_file_provenance, iso_now, review_note_provenance


PAIR_ARG_SEPARATOR = "::"


@dataclass(frozen=True)
class SkippedPair:
    note_path: str
    gate_id: str
    reason: str


@dataclass(frozen=True)
class PreparedBatch:
    targets: list[NoteReviewTarget]
    skipped: list[SkippedPair]
    prompt_path: str
    bundle_output_path: str


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


def batch_artifact_dir(repo_root: Path, first_review_run_id: int) -> Path:
    return repo_root / BUNDLE_ARTIFACTS_ROOT / f"review-batch-{first_review_run_id}"


def prepare_review_batch(
    *,
    repo_root: Path,
    db_path: Path,
    pairs: list[tuple[str, str]],
    runner: str,
    model_id: str,
) -> PreparedBatch:
    """Create one review run per note for the given pairs and render the
    batch prompt. Inapplicable gates are skipped and reported, not fatal;
    a missing note or gate file, or a dirty gate, is fatal (ValueError)."""
    gates_dir = repo_root / GATES_ROOT

    grouped: dict[str, list[str]] = {}
    for note_path, gate_id in pairs:
        grouped.setdefault(note_path, []).append(gate_id)

    skipped: list[SkippedPair] = []
    note_gates: dict[str, list[str]] = {}
    for note_path, gate_ids in grouped.items():
        note_abs = repo_root / note_path
        if not note_abs.is_file():
            raise ValueError(f"note not found: {note_path}")
        applicable = applicable_gate_ids_for_note(note_abs, gate_ids, gates_dir)
        for gate_id in gate_ids:
            if gate_id not in applicable:
                skipped.append(SkippedPair(note_path=note_path, gate_id=gate_id, reason="not applicable"))
        if applicable:
            note_gates[note_path] = applicable

    if not note_gates:
        raise ValueError("no applicable pairs to prepare")

    gate_shas: dict[str, str] = {}
    gate_texts: dict[str, str] = {}
    for gate_id in sorted({gate_id for gate_ids in note_gates.values() for gate_id in gate_ids}):
        gate_abs = gates_dir / f"{gate_id}.md"
        if not gate_abs.is_file():
            raise ValueError(f"gate not found: {gate_id}")
        gate_shas[gate_id], _ = committed_file_provenance(repo_root, gate_abs, kind="gate")
        gate_texts[gate_id] = frontmatter.strip(gate_abs.read_text(encoding="utf-8")).lstrip("\n")

    started_at = iso_now()
    targets: list[NoteReviewTarget] = []
    with connect(db_path) as conn:
        for note_path, gate_ids in note_gates.items():
            note_sha, note_commit = review_note_provenance(repo_root, Path(note_path))
            review_run_id = create_run(
                conn,
                note_path=note_path,
                model_id=model_id,
                runner=runner,
                reviewed_note_sha=note_sha,
                reviewed_note_commit=note_commit,
                started_at=started_at,
                gates=[(gate_id, gate_shas[gate_id], ordinal) for ordinal, gate_id in enumerate(gate_ids)],
            )
            bundle_artifact_dir(repo_root, review_run_id).mkdir(parents=True, exist_ok=True)
            targets.append(
                prepare_note_target(
                    repo_root=repo_root,
                    note_path=note_path,
                    review_run_id=review_run_id,
                    gate_ids=tuple(gate_ids),
                )
            )
        conn.commit()

    batch_dir = batch_artifact_dir(repo_root, targets[0].review_run_id)
    bundle_output_path = (batch_dir / "bundle-output.md").relative_to(repo_root).as_posix()
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
            review_run_ids=[target.review_run_id for target in targets],
            failure_reason=str(exc),
        )
        raise

    batch_dir.mkdir(parents=True, exist_ok=True)
    prompt_abs = batch_dir / "prompt.md"
    prompt_abs.write_text(prompt, encoding="utf-8")

    return PreparedBatch(
        targets=targets,
        skipped=skipped,
        prompt_path=prompt_abs.relative_to(repo_root).as_posix(),
        bundle_output_path=bundle_output_path,
    )


def ingest_batch_output(
    *,
    repo_root: Path,
    db_path: Path,
    review_run_ids: list[int],
    raw_bundle_markdown: str,
) -> tuple[list[int], list[tuple[int, str]]]:
    """Parse a batch's pair output and finalize its runs with salvage.

    Structural parse errors fail every listed run and raise ValueError;
    missing pairs fail only their run. Returns (completed, failed)."""
    run_pairs: list[RunPairs] = []
    with connect(db_path) as conn:
        for review_run_id in review_run_ids:
            review_run = load_review_run(conn, review_run_id=review_run_id)
            if review_run is None:
                raise ValueError(f"review run not found: {review_run_id}")
            if review_run.status != "running":
                raise ValueError(f"review run is not ingestible: {review_run_id} ({review_run.status})")
            gate_ids = tuple(row.gate_id for row in load_review_run_gates(conn, review_run_id=review_run_id))
            run_pairs.append(RunPairs(note_path=review_run.note_path, review_run_id=review_run_id, gate_ids=gate_ids))

    note_paths = [run.note_path for run in run_pairs]
    if len(set(note_paths)) != len(note_paths):
        raise ValueError("review runs in one batch must target distinct notes")

    expected_pairs = [(run.note_path, gate_id) for run in run_pairs for gate_id in run.gate_ids]
    try:
        parsed = parse_pair_bundle(raw_bundle_markdown, expected_pairs=expected_pairs)
    except ValueError as exc:
        fail_running_review_runs(
            db_path=db_path,
            review_run_ids=[run.review_run_id for run in run_pairs],
            failure_reason=str(exc),
            raw_bundle_markdown=raw_bundle_markdown,
        )
        raise

    return finalize_runs_from_parsed(
        repo_root=repo_root,
        db_path=db_path,
        run_pairs=run_pairs,
        parsed=parsed,
        raw_output=raw_bundle_markdown,
    )
