"""Shared helpers for external content snapshots."""

from __future__ import annotations

from pathlib import Path


def dedup_existing_snapshot(out_dir: Path, source_url: str) -> Path | None:
    """Return an existing markdown snapshot path for source_url, if present."""
    # Newline-terminated so a URL that prefixes another URL never matches it
    # (issues/12 vs issues/123). Snapshot frontmatter always writes the line
    # with a trailing newline.
    marker = f"source: {source_url}\n"
    for existing in out_dir.glob("*.md"):
        try:
            header = existing.read_text(encoding="utf-8")[:1000]
        except OSError:
            continue
        if marker in header:
            return existing
    return None
