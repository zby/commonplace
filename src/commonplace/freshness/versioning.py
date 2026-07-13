"""Path versioning for freshness inputs."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from commonplace.lib.hashing import content_sha256_for_text
from commonplace.review.paths import normalize_repo_relative_path

FILE_TEXT = "file-text"


@dataclass(frozen=True)
class ResolvedVersion:
    artifact_path: str
    version_kind: str
    content_text: str
    content_sha256: str


def resolve_file_text(*, repo_root: Path, path: str) -> ResolvedVersion:
    normalized_path = normalize_repo_relative_path(path, label="artifact path")
    file_path = repo_root / normalized_path
    if not file_path.is_file():
        raise FileNotFoundError(f"artifact not found: {normalized_path}")
    content_text = file_path.read_text(encoding="utf-8")
    return ResolvedVersion(
        artifact_path=normalized_path,
        version_kind=FILE_TEXT,
        content_text=content_text,
        content_sha256=content_sha256_for_text(content_text),
    )