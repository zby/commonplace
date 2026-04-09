"""Shared naming rules and slug helpers."""

from __future__ import annotations

import re
from pathlib import Path


MAX_NOTE_TITLE_LENGTH = 100
MAX_NOTE_SLUG_LENGTH = 100
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
