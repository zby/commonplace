"""Shared naming rules and slug helpers."""

from __future__ import annotations

import re
from pathlib import Path

MAX_NOTE_TITLE_LENGTH = 100
MAX_NOTE_SLUG_LENGTH = 70
INGEST_DERIVED_STEM_SUFFIX = ".ingest"
MAX_INGEST_SNAPSHOT_SLUG_LENGTH = MAX_NOTE_SLUG_LENGTH - len(
    INGEST_DERIVED_STEM_SUFFIX
)
_NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")


def slugify_text(
    text: str,
    *,
    max_len: int | None = None,
    default: str | None = None,
) -> str:
    slug = _NON_ALNUM_RE.sub("-", text.strip().lower()).strip("-")
    if max_len is not None:
        slug = slug[:max_len].rstrip("-")
    if slug:
        return slug
    if default is not None:
        return default
    raise ValueError(f"Could not derive a slug from: {text!r}")


def slugify_text_with_suffix(
    text: str,
    suffix: str,
    *,
    max_len: int,
    default: str,
) -> str:
    """Slugify text while reserving room for a stable hyphenated suffix."""
    suffix_slug = slugify_text(suffix)
    reserved_suffix = f"-{suffix_slug}"
    prefix_max_len = max_len - len(reserved_suffix)
    if prefix_max_len < 1:
        raise ValueError(
            f"suffix leaves no room for a slug within {max_len} characters: "
            f"{suffix_slug!r}"
        )
    prefix = slugify_text(text, max_len=prefix_max_len, default=default)
    if len(prefix) > prefix_max_len:
        prefix = slugify_text(prefix, max_len=prefix_max_len)
    return f"{prefix}{reserved_suffix}"


def ensure_note_slug_length(slug: str) -> None:
    if len(slug) > MAX_NOTE_SLUG_LENGTH:
        raise ValueError(
            f"note filename slug exceeds {MAX_NOTE_SLUG_LENGTH} characters: {len(slug)}"
        )


def slugify_note_filename(text: str) -> str:
    stem = Path(text.strip()).stem
    slug = slugify_text(stem)
    ensure_note_slug_length(slug)
    return slug
