"""MkDocs hooks: inject note metadata badge, generate top-level collection nav."""

import os
import re
from pathlib import Path

from commonplace.lib import frontmatter


def on_config(config):
    """Generate top-level nav from kb/<collection>/README.md files.

    Any directory directly under docs_dir containing a README.md becomes a
    top-nav entry pointing at that README. Discovery is alphabetical;
    fixed Home and external entries bracket the auto-discovered list.
    """
    docs_dir = Path(config["docs_dir"])
    collection_entries = []
    for child in sorted(docs_dir.iterdir()):
        if not child.is_dir() or child.name.startswith("."):
            continue
        readme = child / "README.md"
        if not readme.exists():
            continue
        label = child.name.replace("-", " ").title()
        collection_entries.append({label: str(readme.relative_to(docs_dir))})

    # TODO: read external links (Recent Changes, GitHub, etc.) from mkdocs.yml
    # so consuming projects don't have to fork this hook to change them.
    config["nav"] = [
        {"Home": "index.md"},
        *collection_entries,
        {"Recent Changes": "https://github.com/zby/commonplace/commits/main/"},
        {"GitHub": "https://github.com/zby/commonplace"},
    ]
    return config


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
