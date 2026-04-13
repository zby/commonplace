"""Shared helpers for external content snapshots."""

from __future__ import annotations

from pathlib import Path


def dedup_existing_snapshot(out_dir: Path, source_url: str) -> Path | None:
    """Return an existing markdown snapshot path for source_url, if present."""
    marker = f"source: {source_url}"
    for existing in out_dir.glob("*.md"):
        try:
            header = existing.read_text(encoding="utf-8")[:1000]
        except OSError:
            continue
        if marker in header:
            return existing
    return None
