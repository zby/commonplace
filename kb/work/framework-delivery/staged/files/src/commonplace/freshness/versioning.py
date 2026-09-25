"""Path versioning for freshness inputs."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from commonplace.lib.hashing import content_sha256_for_text
from commonplace.lib.library import artifact_file, is_library_identity
from commonplace.review.paths import normalize_repo_relative_path

FILE_TEXT = "file-text"


@dataclass(frozen=True)
class ResolvedVersion:
    artifact_path: str
    version_kind: str
    content_text: str
    content_sha256: str


def resolve_file_text_content(
    *, repo_root: Path, path: str, content_text: str
) -> ResolvedVersion:
    """Resolve supplied text under the identity of one repository path or library file."""
    normalized_path = _normalize_identity(repo_root, path)
    return ResolvedVersion(
        artifact_path=normalized_path,
        version_kind=FILE_TEXT,
        content_text=content_text,
        content_sha256=content_sha256_for_text(content_text),
    )


def _normalize_identity(repo_root: Path, path: str) -> str:
    """A repo-relative path that stays in the repository, or a `commonplace:` library identity."""
    if is_library_identity(path):
        artifact_file(repo_root, path)  # rejects identities that escape the library
        return path
    normalized_path = normalize_repo_relative_path(path, label="artifact path")
    file_path = (repo_root / normalized_path).resolve()
    try:
        file_path.relative_to(repo_root.resolve())
    except ValueError as exc:
        raise ValueError(f"artifact path escapes repository: {normalized_path}") from exc
    return normalized_path


def resolve_file_text(*, repo_root: Path, path: str) -> ResolvedVersion:
    normalized_path = _normalize_identity(repo_root, path)
    file_path = artifact_file(repo_root, normalized_path)
    if not file_path.is_file():
        raise FileNotFoundError(f"artifact not found: {normalized_path}")
    content_text = file_path.read_text(encoding="utf-8")
    return resolve_file_text_content(
        repo_root=repo_root,
        path=normalized_path,
        content_text=content_text,
    )
