"""Filesystem artifacts for review jobs."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Protocol, Sequence

import yaml


MANIFEST_NAME = "MANIFEST.json"
BUNDLE_ARTIFACTS_ROOT = Path("kb/reports/bundle-reviews")


class ReviewPairForPath(Protocol):
    review_pair_id: int
    note_path: str
    gate_path: str
    pair_ordinal: int


class ReviewJobForResult(Protocol):
    review_job_id: int
    model_partition: str
    runner: str | None
    runner_model: str | None
    runner_effort: str | None
    packing: str


class ReviewPairForResult(Protocol):
    review_pair_id: int
    review_job_id: int
    note_path: str
    gate_path: str
    model_partition: str
    pair_ordinal: int
    result_kind: str
    decision: str | None
    reviewed_at: str | None


class SkippedPairForManifest(Protocol):
    note_path: str
    gate_path: str
    reason: str


def bundle_artifact_dir(repo_root: Path, review_job_id: int) -> Path:
    return repo_root / review_job_artifact_dir_rel(review_job_id)


def review_job_artifact_dir_rel(review_job_id: int) -> str:
    return (BUNDLE_ARTIFACTS_ROOT / f"review-job-{review_job_id}").as_posix()


def prompt_path_rel(review_job_id: int) -> str:
    return f"{review_job_artifact_dir_rel(review_job_id)}/prompt.md"


def bundle_output_path_rel(review_job_id: int) -> str:
    return f"{review_job_artifact_dir_rel(review_job_id)}/bundle-output.md"


def manifest_path_rel(review_job_id: int) -> str:
    return f"{review_job_artifact_dir_rel(review_job_id)}/{MANIFEST_NAME}"


def result_filename(
    *,
    packing: str,
    note_path: str,
    gate_path: str,
    pair_ordinal: int,
) -> str:
    """Per-pair result filename, a pure function of the pair row.

    The ordinal guarantees uniqueness inside the job; the stem names the
    axis that varies within the packing. Deriving from the pair row alone
    keeps the filename stable when sibling pairs are later pruned.
    """
    if packing == "note":
        stem = Path(gate_path).stem
    elif packing == "gate":
        stem = Path(note_path).stem
    else:
        raise ValueError(f"unsupported review job packing: {packing}")
    return f"pair-{pair_ordinal}-{stem}.md"


def result_path(
    *,
    review_job_id: int,
    packing: str,
    note_path: str,
    gate_path: str,
    pair_ordinal: int,
) -> str:
    return (
        f"{review_job_artifact_dir_rel(review_job_id)}/"
        f"{result_filename(packing=packing, note_path=note_path, gate_path=gate_path, pair_ordinal=pair_ordinal)}"
    )


def result_paths_by_pair_id(
    *,
    review_job_id: int,
    packing: str,
    pairs: Sequence[ReviewPairForPath],
) -> dict[int, str]:
    return {
        pair.review_pair_id: result_path(
            review_job_id=review_job_id,
            packing=packing,
            note_path=pair.note_path,
            gate_path=pair.gate_path,
            pair_ordinal=pair.pair_ordinal,
        )
        for pair in pairs
    }


def repo_relative_path(repo_root: Path, relative_path: str, *, label: str) -> Path:
    path = Path(relative_path)
    if path.is_absolute():
        raise ValueError(f"{label} must be repo-relative: {relative_path}")
    target = (repo_root / path).resolve()
    repo_root_resolved = repo_root.resolve()
    if not target.is_relative_to(repo_root_resolved):
        raise ValueError(f"{label} escapes repo root: {relative_path}")
    return target


def result_frontmatter(
    *,
    job: ReviewJobForResult,
    pair: ReviewPairForResult,
) -> str:
    payload = {
        "review_job_id": job.review_job_id,
        "review_pair_id": pair.review_pair_id,
        "note_path": pair.note_path,
        "gate_path": pair.gate_path,
        "model_partition": job.model_partition,
        "runner": job.runner,
        "runner_model": job.runner_model,
        "runner_effort": job.runner_effort,
        "result_kind": pair.result_kind,
        "decision": pair.decision,
        "reviewed_at": pair.reviewed_at,
    }
    return "---\n" + yaml.safe_dump(payload, allow_unicode=False, sort_keys=False) + "---\n"


def write_pair_result_files_to_derived_paths(
    *,
    repo_root: Path,
    job: ReviewJobForResult,
    pairs: Sequence[ReviewPairForResult],
    canonical_texts: dict[tuple[str, str], str],
) -> None:
    pending_writes: list[tuple[Path, str]] = []
    result_paths = result_paths_by_pair_id(
        review_job_id=job.review_job_id,
        packing=job.packing,
        pairs=pairs,
    )
    for pair in pairs:
        if pair.reviewed_at is None:
            continue
        review_text = canonical_texts.get((pair.note_path, pair.gate_path))
        if review_text is None:
            continue
        output_path = repo_relative_path(
            repo_root,
            result_paths[pair.review_pair_id],
            label="result_path",
        )
        pending_writes.append(
            (
                output_path,
                result_frontmatter(job=job, pair=pair) + review_text,
            )
        )

    for output_path, content in pending_writes:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding="utf-8")


def write_manifest(
    *,
    repo_root: Path,
    artifact_dir: Path,
    review_job_id: int,
    job_status: str,
    packing: str,
    prompt_path: str,
    bundle_output_path: str,
    pairs: Sequence[ReviewPairForPath],
    skipped: Sequence[SkippedPairForManifest] | None = None,
    failure_reason: str | None = None,
) -> str:
    result_paths = result_paths_by_pair_id(
        review_job_id=review_job_id,
        packing=packing,
        pairs=pairs,
    )
    payload_pairs: list[dict[str, object]] = []
    pair_display_status = {
        "queued": "pending",
        "completed": "completed",
        "failed": "failed",
    }.get(job_status, job_status)
    for pair in pairs:
        item: dict[str, object] = {
            "review_pair_id": pair.review_pair_id,
            "note_path": pair.note_path,
            "gate_path": pair.gate_path,
            "result_kind": getattr(pair, "result_kind", "verdict"),
            "status": pair_display_status,
            "result_path": result_paths[pair.review_pair_id],
        }
        if failure_reason is not None:
            item["failure_reason"] = failure_reason
        payload_pairs.append(item)

    payload: dict[str, object] = {
        "artifact_schema": "review-job-prompt-v2",
        "review_job_id": review_job_id,
        "status": job_status,
        "packing": packing,
        "prompt_path": prompt_path,
        "bundle_output_path": bundle_output_path,
        "pairs": payload_pairs,
        "skipped_pairs": [
            {"note_path": pair.note_path, "gate_path": pair.gate_path, "reason": pair.reason}
            for pair in (skipped or [])
        ],
    }
    manifest_path = artifact_dir / MANIFEST_NAME
    artifact_dir.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(payload, ensure_ascii=True, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest_path.relative_to(repo_root).as_posix()
