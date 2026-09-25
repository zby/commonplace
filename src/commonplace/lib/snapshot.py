"""Shared helpers for local external-source snapshots."""

from __future__ import annotations

import hashlib
import os
import re
from dataclasses import dataclass, field
from pathlib import Path

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
    for name in ("captured", "capture"):
        if name not in metadata or metadata[name] in (None, ""):
            raise ValueError(f"snapshot frontmatter must contain {name}")
    return metadata


# The path forms earlier releases wrote; the line may close the frontmatter block.
_RETIRED_SNAPSHOT_TYPE = re.compile(
    rb"^type: (?:kb/sources/types/|\./types/)snapshot\.md(?=\r?\n|\Z)", re.MULTILINE
)
_CURRENT_SNAPSHOT_TYPE = b"type: snapshot"
_PINNED_CHECKSUM = re.compile(
    rb"^((?:original_)?snapshot_sha256:[ \t]*)([0-9a-f]{64})(?=[ \t]*\r?$)", re.MULTILINE
)


@dataclass
class SnapshotTypeMigration:
    rewritten_snapshots: list[Path] = field(default_factory=list)
    repinned_ingests: list[Path] = field(default_factory=list)


def _split_frontmatter(data: bytes) -> tuple[bytes, bytes] | None:
    if not data.startswith(b"---"):
        return None
    end = data.find(b"\n---", 3)
    return None if end == -1 else (data[:end], data[end:])


def _retyped_snapshot_bytes(data: bytes) -> bytes | None:
    """The capture with its retired type line replaced, or None if it has none.

    Only the frontmatter line changes, so the result is the same on every
    machine that holds the same capture bytes.
    """
    parts = _split_frontmatter(data)
    if parts is None:
        return None
    head, rest = parts
    new_head, count = _RETIRED_SNAPSHOT_TYPE.subn(_CURRENT_SNAPSHOT_TYPE, head, count=1)
    return new_head + rest if count else None


def migrate_snapshot_types(kb_dir: Path) -> SnapshotTypeMigration:
    """Retype captures that still name a retired snapshot type path (ADR 087 draft).

    Every capture under a `.snapshots/` directory whose frontmatter has a retired
    `type:` line is rewritten to `type: snapshot`; nothing else in it changes.
    An ingest beside that directory that pins the capture's old bytes through
    `snapshot_sha256` or `original_snapshot_sha256` is re-pinned to the new
    bytes. An ingest that already pins the new bytes (another clone migrated
    it) and a capture that no ingest pins need nothing more. Running it again
    changes nothing.
    """
    result = SnapshotTypeMigration()
    snapshot_dirs = sorted(
        Path(dirpath) / ".snapshots"
        for dirpath, dirnames, _ in os.walk(kb_dir)
        if ".snapshots" in dirnames
    )
    for snapshot_dir in snapshot_dirs:
        _migrate_snapshot_dir(snapshot_dir, result)
    return result


def _migrate_snapshot_dir(snapshot_dir: Path, result: SnapshotTypeMigration) -> None:
    # Checksum of a capture's current bytes -> (capture, rewritten bytes, their checksum).
    by_old: dict[str, tuple[Path, bytes, str]] = {}
    for path in sorted(snapshot_dir.glob("*.md")):
        if path.is_symlink() or not path.is_file():
            continue
        data = path.read_bytes()
        new_data = _retyped_snapshot_bytes(data)
        if new_data is None:
            continue
        new_hash = hashlib.sha256(new_data).hexdigest()
        by_old[hashlib.sha256(data).hexdigest()] = (path, new_data, new_hash)

    def repin(match: re.Match[bytes]) -> bytes:
        pinned = match.group(2).decode()
        if pinned in by_old:
            return match.group(1) + by_old[pinned][2].encode()
        return match.group(0)

    for ingest in sorted(snapshot_dir.parent.glob("*.ingest.md")):
        parts = _split_frontmatter(ingest.read_bytes())
        if parts is None:
            continue
        head, rest = parts
        new_head = _PINNED_CHECKSUM.sub(repin, head)
        if new_head != head:
            ingest.write_bytes(new_head + rest)
            result.repinned_ingests.append(ingest)
    for path, new_data, _ in sorted(by_old.values()):
        path.write_bytes(new_data)
        result.rewritten_snapshots.append(path)


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
