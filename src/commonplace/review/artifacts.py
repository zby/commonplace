"""Filesystem artifacts for review jobs."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Protocol, Sequence

import yaml


MANIFEST_NAME = "MANIFEST.json"
BUNDLE_ARTIFACTS_ROOT = Path("kb/reports/bundle-reviews")


class ReviewPairForManifest(Protocol):
    review_pair_id: int
    note_path: str
    gate_path: str
    result_path: str | None


class ReviewPairForPath(Protocol):
    review_pair_id: int
    note_path: str
    gate_path: str


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
    decision: str | None
    result_path: str | None
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


def encode_stage_filename(gate_path: str) -> str:
    return Path(gate_path).with_suffix("").as_posix().replace("/", "__") + ".md"


def _note_filename(note_path: str, all_note_paths: Sequence[str]) -> str:
    name = Path(note_path).name
    all_names = [Path(path).name for path in all_note_paths]
    if all_names.count(name) == 1:
        return name
    return note_path.replace("/", "__")


def result_filename(
    *,
    packing: str,
    note_path: str,
    gate_path: str,
    all_note_paths: Sequence[str],
) -> str:
    if packing == "note":
        return Path(gate_path).name
    if packing == "gate":
        return _note_filename(note_path, all_note_paths)
    raise ValueError(f"unsupported review job packing: {packing}")


def result_path(
    *,
    review_job_id: int,
    packing: str,
    note_path: str,
    gate_path: str,
    all_note_paths: Sequence[str],
) -> str:
    return (
        f"{review_job_artifact_dir_rel(review_job_id)}/"
        f"{result_filename(packing=packing, note_path=note_path, gate_path=gate_path, all_note_paths=all_note_paths)}"
    )


def result_paths_by_pair_id(
    *,
    review_job_id: int,
    packing: str,
    pairs: Sequence[ReviewPairForPath],
) -> dict[int, str]:
    all_note_paths = [pair.note_path for pair in pairs]
    return {
        pair.review_pair_id: result_path(
            review_job_id=review_job_id,
            packing=packing,
            note_path=pair.note_path,
            gate_path=pair.gate_path,
            all_note_paths=all_note_paths,
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


def write_pair_result_files(
    *,
    artifact_dir: Path,
    packing: str,
    pairs: Sequence[tuple[str, str]],
    canonical_texts: dict[tuple[str, str], str],
) -> None:
    all_note_paths = [note_path for note_path, _ in pairs]
    artifact_dir.mkdir(parents=True, exist_ok=True)
    for note_path, gate_path in pairs:
        review_text = canonical_texts.get((note_path, gate_path))
        if review_text is None:
            continue
        filename = result_filename(
            packing=packing,
            note_path=note_path,
            gate_path=gate_path,
            all_note_paths=all_note_paths,
        )
        output_path = (artifact_dir / filename).resolve()
        if not output_path.is_relative_to(artifact_dir.resolve()):
            raise ValueError(f"result filename escapes artifact dir: {filename}")
        output_path.write_text(review_text, encoding="utf-8")


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
        if pair.decision is None:
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
    pairs: Sequence[ReviewPairForManifest],
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
            "status": pair_display_status,
            "result_path": pair.result_path or result_paths[pair.review_pair_id],
        }
        if failure_reason is not None:
            item["failure_reason"] = failure_reason
        payload_pairs.append(item)

    payload: dict[str, object] = {
        "artifact_schema": "review-job-prompt-v1",
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
