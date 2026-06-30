"""Filesystem artifacts for review jobs."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Protocol, Sequence


MANIFEST_NAME = "MANIFEST.json"


class ReviewPairForManifest(Protocol):
    review_pair_id: int
    note_path: str
    gate_path: str
    pair_status: str


class SkippedPairForManifest(Protocol):
    note_path: str
    gate_path: str
    reason: str


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
    artifact_dir_rel: str,
    packing: str,
    note_path: str,
    gate_path: str,
    all_note_paths: Sequence[str],
) -> str:
    return (
        f"{artifact_dir_rel}/"
        f"{result_filename(packing=packing, note_path=note_path, gate_path=gate_path, all_note_paths=all_note_paths)}"
    )


def result_paths_by_pair_id(
    *,
    artifact_dir_rel: str,
    packing: str,
    pairs: Sequence[ReviewPairForManifest],
) -> dict[int, str]:
    all_note_paths = [pair.note_path for pair in pairs]
    return {
        pair.review_pair_id: result_path(
            artifact_dir_rel=artifact_dir_rel,
            packing=packing,
            note_path=pair.note_path,
            gate_path=pair.gate_path,
            all_note_paths=all_note_paths,
        )
        for pair in pairs
    }


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
        (artifact_dir / filename).write_text(review_text, encoding="utf-8")


def write_manifest(
    *,
    repo_root: Path,
    artifact_dir: Path,
    review_job_id: int,
    packing: str,
    prompt_path: str,
    bundle_output_path: str,
    pairs: Sequence[ReviewPairForManifest],
    skipped: Sequence[SkippedPairForManifest] | None = None,
    failure_reason: str | None = None,
) -> str:
    artifact_dir_rel = artifact_dir.relative_to(repo_root).as_posix()
    result_paths = result_paths_by_pair_id(
        artifact_dir_rel=artifact_dir_rel,
        packing=packing,
        pairs=pairs,
    )
    payload_pairs: list[dict[str, object]] = []
    for pair in pairs:
        item: dict[str, object] = {
            "review_pair_id": pair.review_pair_id,
            "note_path": pair.note_path,
            "gate_path": pair.gate_path,
            "status": pair.pair_status,
            "result_path": result_paths[pair.review_pair_id],
        }
        if failure_reason is not None:
            item["failure_reason"] = failure_reason
        payload_pairs.append(item)

    payload: dict[str, object] = {
        "artifact_schema": "review-job-prompt-v1",
        "review_job_id": review_job_id,
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
