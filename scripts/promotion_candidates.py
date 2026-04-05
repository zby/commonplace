#!/usr/bin/env python3
"""Generate a promotion candidates report for kb/notes/.

Surfaces two kinds of candidates:
- text → note: files without frontmatter that have incoming links from notes
- seedling → current: seedling notes with high incoming link counts

Writes the report to kb/reports/promotion-candidates.md.

Usage: python3 scripts/promotion_candidates.py
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

import frontmatter as fm_mod

NOTES_DIR = Path("kb/notes")
REPORTS_DIR = Path("kb/reports")


def parse_frontmatter(content: str) -> dict | None:
    """Parse frontmatter, returning None for genuine text files (no delimiters)."""
    if not content.startswith("---\n"):
        return None
    result = fm_mod.parse(content)
    return result.data


def get_title(content: str) -> str:
    """Extract first H1 heading from markdown."""
    body = fm_mod.strip(content)
    match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    return match.group(1) if match else "Untitled"


def extract_links(content: str) -> list[str]:
    """Extract markdown link targets from content."""
    return re.findall(r"\[[^\]]*\]\(([^)]+)\)", content)


def resolve_link(source: Path, target: str) -> Path | None:
    """Resolve a relative link target to an absolute path."""
    if target.startswith("http://") or target.startswith("https://"):
        return None
    # Strip anchors
    target = target.split("#")[0]
    if not target:
        return None
    resolved = (source.parent / target).resolve()
    return resolved


def main() -> None:
    if not NOTES_DIR.is_dir():
        print(f"Not a directory: {NOTES_DIR}", file=sys.stderr)
        sys.exit(1)

    # Classify all notes
    text_files: dict[Path, str] = {}  # path -> title
    seedlings: dict[Path, str] = {}  # path -> title
    all_notes: dict[Path, dict] = {}  # path -> {fm, title, content}

    for path in sorted(NOTES_DIR.rglob("*.md")):
        if path.name in ("index.md", "README.md"):
            continue
        if "types" in path.relative_to(NOTES_DIR).parts:
            continue

        abs_path = path.resolve()
        content = path.read_text(encoding="utf-8")
        fm = parse_frontmatter(content)
        title = get_title(content)
        all_notes[abs_path] = {"fm": fm, "title": title, "content": content, "rel": path}

        if fm is None:
            text_files[abs_path] = title
        elif fm.get("status") == "seedling":
            seedlings[abs_path] = title

    # Build incoming link counts
    incoming_links: dict[Path, list[Path]] = defaultdict(list)
    for source_path, info in all_notes.items():
        links = extract_links(info["content"])
        for link in links:
            resolved = resolve_link(info["rel"], link)
            if resolved and resolved in all_notes:
                incoming_links[resolved].append(source_path)

    # Text files with incoming links
    text_with_links = []
    for path, title in sorted(text_files.items()):
        sources = incoming_links.get(path, [])
        real_sources = [
            s for s in sources if all_notes[s]["rel"].name != "index.md"
        ]
        rel = all_notes[path]["rel"].relative_to(NOTES_DIR)
        text_with_links.append((rel, title, len(real_sources), real_sources))

    text_with_links.sort(key=lambda x: (-x[2], str(x[0])))

    # Seedlings ranked by incoming link count
    seedling_ranked = []
    for path, title in sorted(seedlings.items()):
        sources = incoming_links.get(path, [])
        real_sources = [
            s for s in sources if all_notes[s]["rel"].name != "index.md"
        ]
        rel = all_notes[path]["rel"].relative_to(NOTES_DIR)
        seedling_ranked.append((rel, title, len(real_sources), real_sources))

    seedling_ranked.sort(key=lambda x: (-x[2], str(x[0])))

    # Build report
    lines = [
        f"# Promotion Candidates — {date.today()}",
        "",
        f"Text files: {len(text_files)} | Seedlings: {len(seedlings)}",
        "",
    ]

    # Text → note section
    lines.append("## Text → Note")
    lines.append("")
    if text_with_links:
        for rel, title, count, sources in text_with_links:
            source_list = ", ".join(
                f"[{all_notes[s]['title']}](../notes/{all_notes[s]['rel'].relative_to(NOTES_DIR)})"
                for s in sources[:3]
            )
            if len(sources) > 3:
                source_list += f" +{len(sources) - 3} more"
            lines.append(f"- [{title}](../notes/{rel}) — **{count} links in**")
            if source_list:
                lines.append(f"  Sources: {source_list}")
            lines.append("")
    else:
        lines.append("No text files found.")
        lines.append("")

    # Seedling → current section
    lines.append("## Seedling → Current (top 20 by incoming links)")
    lines.append("")
    top_seedlings = seedling_ranked[:20]
    if top_seedlings:
        for rel, title, count, sources in top_seedlings:
            source_list = ", ".join(
                f"[{all_notes[s]['title']}](../notes/{all_notes[s]['rel'].relative_to(NOTES_DIR)})"
                for s in sources[:3]
            )
            if len(sources) > 3:
                source_list += f" +{len(sources) - 3} more"
            lines.append(f"- [{title}](../notes/{rel}) — **{count} links in**")
            if source_list:
                lines.append(f"  Sources: {source_list}")
            lines.append("")
    else:
        lines.append("No seedling notes found.")
        lines.append("")
    lines.append("")

    # Orphan seedlings (zero incoming links)
    orphan_seedlings = [x for x in seedling_ranked if x[2] == 0]
    if orphan_seedlings:
        lines.append(f"## Orphan Seedlings ({len(orphan_seedlings)} with zero incoming links)")
        lines.append("")
        for rel, title, _, _ in orphan_seedlings:
            lines.append(f"- [{title}](../notes/{rel})")
        lines.append("")

    output = REPORTS_DIR / "promotion-candidates.md"
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {output} ({len(text_files)} text, {len(seedlings)} seedlings)")


if __name__ == "__main__":
    main()
