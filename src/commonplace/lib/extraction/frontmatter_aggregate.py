"""Aggregate frontmatter field values across a KB tree."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable
from pathlib import Path

from commonplace.lib import frontmatter


def aggregate_field(
    field: str,
    *,
    roots: Iterable[Path],
    glob: str = "*.md",
) -> dict[str, list[Path]]:
    """Return ``{value: [files]}`` for ``field`` across markdown files under roots.

    Files without frontmatter, or without the field, are skipped silently.
    Symlinks are skipped. Values are stringified with ``str()`` for keying;
    non-string values (lists, dicts, numbers) are stored as their ``repr()``.
    """
    out: dict[str, list[Path]] = defaultdict(list)
    for root in roots:
        for md in sorted(Path(root).rglob(glob)):
            if md.is_symlink() or not md.is_file():
                continue
            text = md.read_text(encoding="utf-8", errors="replace")
            parsed = frontmatter.parse(text)
            if not parsed.ok or not parsed.data:
                continue
            if field not in parsed.data:
                continue
            value = parsed.data[field]
            key = value if isinstance(value, str) else repr(value)
            out[key].append(md)
    return dict(out)
