"""Shared helpers for local external-source snapshots."""

from __future__ import annotations

import hashlib
from datetime import date
from pathlib import Path

from commonplace.lib import frontmatter

SNAPSHOT_DIR = Path("kb/sources/.snapshots")


def snapshot_sha256(path: Path) -> str:
    """Return lowercase SHA-256 of the exact bytes stored at ``path``."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def reobservation_slug(slug: str, captured: date, max_len: int) -> str:
    """A distinct basename for a new capture of an already captured source.

    The earlier capture stays pinned by its ingest; the new observation gets its
    own file, named by the capture date, and its own ingest.
    """
    suffix = f"-{captured:%Y%m%d}"
    return slug[: max_len - len(suffix)].rstrip("-") + suffix


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
