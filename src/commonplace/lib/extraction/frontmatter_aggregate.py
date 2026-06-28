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
    Symlinks are skipped. String values are keyed directly. Lists are expanded
    by string item so fields like ``tags`` group by each tag rather than by
    Python container representation. Other non-string values are skipped.
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
            if isinstance(value, str):
                keys = (value,)
            elif isinstance(value, list):
                keys = tuple(item for item in value if isinstance(item, str))
            else:
                continue
            for key in keys:
                out[key].append(md)
    return dict(out)
