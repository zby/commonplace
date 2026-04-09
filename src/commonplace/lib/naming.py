"""Shared naming rules for KB note titles and filename slugs."""

from __future__ import annotations

import re
from pathlib import Path


MAX_NOTE_TITLE_LENGTH = 100
MAX_NOTE_SLUG_LENGTH = 100
_NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")


def ensure_note_slug_length(slug: str) -> None:
    if len(slug) > MAX_NOTE_SLUG_LENGTH:
        raise ValueError(
            f"note filename slug exceeds {MAX_NOTE_SLUG_LENGTH} characters: {len(slug)}"
        )


def slugify_note_filename(text: str) -> str:
    stem = Path(text.strip()).stem
    slug = _NON_ALNUM_RE.sub("-", stem.lower()).strip("-")
    if not slug:
        raise ValueError(f"Could not derive a filename slug from: {text!r}")
    ensure_note_slug_length(slug)
    return slug
