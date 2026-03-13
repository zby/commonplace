"""MkDocs hook: inject note metadata (status, type, tags) below the first heading."""

import os
import re
from pathlib import Path


def _find_tag_index(tag: str, note_dir: Path) -> str | None:
    """Find relative path from note_dir to the tag's index file.

    Searches up to 4 levels above note_dir for {tag}-index.md or {tag}.md,
    both flat and one subdirectory deep.
    """
    filenames = [f"{tag}-index.md", f"{tag}.md"]
    search_dir = note_dir.resolve()
    note_dir_resolved = note_dir.resolve()

    for _ in range(4):
        for filename in filenames:
            candidate = search_dir / filename
            if candidate.exists():
                return os.path.relpath(candidate, note_dir_resolved)

            if search_dir.is_dir():
                for subdir in sorted(search_dir.iterdir()):
                    if subdir.is_dir() and not subdir.name.startswith("."):
                        candidate = subdir / filename
                        if candidate.exists():
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
