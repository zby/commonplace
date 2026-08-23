"""Shared helpers for local external-source snapshots."""

from __future__ import annotations

import hashlib
import re
import shutil
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from commonplace.lib import frontmatter

SNAPSHOT_DIR = Path("kb/sources/.snapshots")
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
_SNAPSHOT_ONLY_FIELDS = frozenset({"description", "genre", "tags", "type"})
_INGEST_COLLISION_FIELDS = frozenset(
    {
        "code_revisions",
        "domains",
        "ingested",
        "secondary_sources",
        "snapshot_sha256",
        "source_snapshot",
    }
)


class DuplicateSnapshotError(RuntimeError):
    """Raised when checksum identity resolves to several local files."""

    def __init__(self, checksum: str, paths: tuple[Path, ...]) -> None:
        self.checksum = checksum
        self.paths = paths
        joined = ", ".join(str(path) for path in paths)
        super().__init__(f"snapshot checksum {checksum} matches multiple files: {joined}")


class SnapshotUnavailableError(RuntimeError):
    """Raised by a recapture adapter when the source cannot be materialized."""


@dataclass(frozen=True)
class SnapshotResolution:
    """Outcome of resolving the observation anchored by one ingest."""

    status: Literal["exact", "mismatch", "unavailable"]
    source: str
    expected_sha256: str
    path: Path | None = None
    actual_sha256: str | None = None
    detail: str | None = None


def snapshot_sha256(path: Path) -> str:
    """Return lowercase SHA-256 of the exact bytes stored at ``path``."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _validate_sha256(checksum: str) -> None:
    if not _SHA256_RE.fullmatch(checksum):
        raise ValueError("snapshot_sha256 must be 64 lowercase hexadecimal characters")


def find_snapshot_by_sha256(snapshot_dir: Path, checksum: str) -> Path | None:
    """Resolve one exact checksum in the flat local snapshot directory."""
    _validate_sha256(checksum)
    if not snapshot_dir.is_dir():
        return None

    matches = tuple(
        path.resolve()
        for path in sorted(snapshot_dir.glob("*.md"))
        if path.is_file() and snapshot_sha256(path) == checksum
    )
    if len(matches) > 1:
        raise DuplicateSnapshotError(checksum, matches)
    return matches[0] if matches else None


def ingest_metadata_from_snapshot(path: Path) -> dict[str, object]:
    """Project capture-owned snapshot frontmatter into a new ingest record."""
    parsed = frontmatter.parse(path.read_text(encoding="utf-8"))
    if not parsed.ok:
        raise ValueError(f"invalid snapshot frontmatter: {'; '.join(parsed.errors)}")

    collisions = sorted(_INGEST_COLLISION_FIELDS.intersection(parsed.data))
    if collisions:
        joined = ", ".join(collisions)
        raise ValueError(f"snapshot metadata collides with ingest fields: {joined}")

    metadata = {
        key: value
        for key, value in parsed.data.items()
        if key not in _SNAPSHOT_ONLY_FIELDS
    }
    source = metadata.get("source")
    if not isinstance(source, str) or not source.startswith(("http://", "https://")):
        raise ValueError("snapshot frontmatter must contain an http(s) source")
    for field in ("captured", "capture"):
        if field not in metadata or metadata[field] in (None, ""):
            raise ValueError(f"snapshot frontmatter must contain {field}")
    return metadata


def _ingest_anchor(ingest_path: Path) -> tuple[str, str]:
    parsed = frontmatter.parse(ingest_path.read_text(encoding="utf-8"))
    if not parsed.ok:
        raise ValueError(f"invalid ingest frontmatter: {'; '.join(parsed.errors)}")

    source = parsed.data.get("source")
    if not isinstance(source, str) or not source.startswith(("http://", "https://")):
        raise ValueError("ingest frontmatter must contain an http(s) source")
    checksum = parsed.data.get("snapshot_sha256")
    if not isinstance(checksum, str):
        raise TypeError("ingest frontmatter must contain snapshot_sha256")
    _validate_sha256(checksum)
    return source, checksum


def _install_exact_snapshot(candidate: Path, snapshot_dir: Path) -> Path:
    """Place an exact recapture in the cache without overwriting other bytes."""
    candidate = candidate.resolve()
    destination_dir = snapshot_dir.resolve()
    if candidate.parent == destination_dir:
        return candidate

    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / candidate.name
    if destination.exists():
        if snapshot_sha256(destination) == snapshot_sha256(candidate):
            return destination
        raise FileExistsError(
            f"refusing to overwrite different local snapshot: {destination}"
        )
    shutil.copyfile(candidate, destination)
    return destination


def resolve_ingest_snapshot(
    ingest_path: Path,
    snapshot_dir: Path,
    *,
    recapture: Callable[[str], Path | None] | None = None,
) -> SnapshotResolution:
    """Resolve an ingest's exact local snapshot, optionally attempting recapture.

    ``recapture`` receives the ingest's canonical source URL. It returns the
    captured Markdown path, ``None`` when unavailable, or raises
    :class:`SnapshotUnavailableError` with an adapter diagnostic. This function
    never edits the ingest or replaces its durable checksum.
    """
    source, expected = _ingest_anchor(ingest_path)
    exact = find_snapshot_by_sha256(snapshot_dir, expected)
    if exact is not None:
        return SnapshotResolution(
            status="exact",
            source=source,
            expected_sha256=expected,
            path=exact,
            actual_sha256=expected,
        )

    if recapture is None:
        return SnapshotResolution(
            status="unavailable",
            source=source,
            expected_sha256=expected,
            detail="no exact local snapshot and no recapture adapter was supplied",
        )

    try:
        candidate = recapture(source)
    except SnapshotUnavailableError as exc:
        return SnapshotResolution(
            status="unavailable",
            source=source,
            expected_sha256=expected,
            detail=str(exc),
        )
    if (
        candidate is None
        or not candidate.is_file()
        or candidate.suffix.lower() != ".md"
    ):
        return SnapshotResolution(
            status="unavailable",
            source=source,
            expected_sha256=expected,
            path=candidate,
            detail="recapture adapter did not produce a Markdown snapshot",
        )

    actual = snapshot_sha256(candidate)
    if actual != expected:
        return SnapshotResolution(
            status="mismatch",
            source=source,
            expected_sha256=expected,
            path=candidate,
            actual_sha256=actual,
            detail=(
                "recapture produced different bytes; the durable checksum was not "
                "updated"
            ),
        )

    installed = _install_exact_snapshot(candidate, snapshot_dir)
    resolved = find_snapshot_by_sha256(snapshot_dir, expected)
    assert resolved == installed
    return SnapshotResolution(
        status="exact",
        source=source,
        expected_sha256=expected,
        path=installed,
        actual_sha256=actual,
        detail="exact bytes reconstructed by recapture",
    )


def dedup_existing_snapshot(out_dir: Path, source_url: str) -> Path | None:
    """Return an existing markdown snapshot path for source_url, if present."""
    for existing in sorted(out_dir.glob("*.md")):
        try:
            header = existing.read_text(encoding="utf-8")[:1000]
        except OSError:
            continue
        parsed = frontmatter.parse(header)
        if parsed.ok and parsed.data.get("source") == source_url:
            return existing
    return None
