"""MkDocs hook: inject note metadata (status, type, tags) below the first heading."""

import os
import re
from pathlib import Path

from commonplace.lib import frontmatter


def _matches_tag_index(candidate: Path, tag: str) -> bool:
    """Return True when a page declares itself as the index for a tag."""
    if not candidate.is_file() or candidate.suffix != ".md":
        return False
    content = candidate.read_text(encoding="utf-8")
    fm = frontmatter.parse(content).data
    return (
        fm.get("type") == "index"
        and fm.get("index_source") == "tag"
        and fm.get("index_key") == tag
    )


def _find_tag_index(tag: str, note_dir: Path) -> str | None:
    """Find relative path from note_dir to the declared index page for a tag."""
    search_dir = note_dir.resolve()
    note_dir_resolved = note_dir.resolve()

    for _ in range(4):
        if search_dir.is_dir():
            for candidate in sorted(search_dir.glob("*.md")):
                if _matches_tag_index(candidate, tag):
                    return os.path.relpath(candidate, note_dir_resolved)
            for subdir in sorted(search_dir.iterdir()):
                if not subdir.is_dir() or subdir.name.startswith("."):
                    continue
                for candidate in sorted(subdir.glob("*.md")):
                    if _matches_tag_index(candidate, tag):
                        return os.path.relpath(candidate, note_dir_resolved)

        search_dir = search_dir.parent

    return None


def on_page_markdown(markdown: str, page, **kwargs) -> str:
    meta = page.meta
    if not meta:
        return markdown

    status = meta.get("status")
    note_type = meta.get("type")
    tags = meta.get("tags", [])
    if not status and not note_type and not tags:
        return markdown

    parts = []
    if note_type:
        parts.append(f"**Type:** {note_type}")
    if status:
        parts.append(f"**Status:** {status}")

    if tags:
        note_dir = Path(page.file.abs_src_path).parent
        tag_links = []
        for tag in tags:
            relpath = _find_tag_index(tag, note_dir)
            if relpath:
                tag_links.append(f"[{tag}]({relpath})")
            else:
                tag_links.append(tag)
        parts.append(f"**Tags:** {', '.join(tag_links)}")

    badge_line = " · ".join(parts)

    # Insert after the first heading
    return re.sub(
        r"(^# .+\n)",
        rf"\1\n{badge_line}\n",
        markdown,
        count=1,
        flags=re.MULTILINE,
    )
