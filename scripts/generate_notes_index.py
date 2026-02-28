#!/usr/bin/env python3
"""Generate index.md from frontmatter of all markdown files in a directory.

Scans all .md files recursively, extracts title, description, and type
from frontmatter, and writes a sorted directory listing to index.md.

Usage: uv run scripts/generate_notes_index.py <directory>
"""

import re
import sys
from pathlib import Path

import yaml


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from markdown content."""
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}


def get_title(content: str) -> str:
    """Extract first H1 heading from markdown."""
    content = re.sub(r"^---\n.*?\n---\n", "", content, flags=re.DOTALL)
    match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    return match.group(1) if match else "Untitled"


def generate(notes_dir: Path) -> str:
    output = notes_dir / "index.md"
    entries: list[tuple[str, str, str, str]] = []  # (rel_path, title, description, type)

    for path in sorted(notes_dir.rglob("*.md")):
        if path == output or path.name == "README.md":
            continue

        content = path.read_text()
        fm = parse_frontmatter(content)
        title = get_title(content)
        desc = fm.get("description", "")
        note_type = fm.get("type", "")
        rel = path.relative_to(notes_dir)

        entries.append((str(rel), title, desc, note_type))

    lines = [
        "---",
        f"description: Auto-generated directory — run scripts/generate_notes_index.py {notes_dir} to rebuild",
        "type: index",
        "---",
        "",
        f"# {notes_dir.name.replace('-', ' ').title()} Directory",
        "",
    ]

    for rel, title, desc, note_type in entries:
        parts = [f"- [{title}](./{rel})"]
        if note_type:
            parts.append(f"*({note_type})*")
        if desc:
            parts.append(f"— {desc}")
        lines.append(" ".join(parts))

    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <directory>", file=sys.stderr)
        sys.exit(1)

    notes_dir = Path(sys.argv[1]).resolve()
    if not notes_dir.is_dir():
        print(f"Not a directory: {notes_dir}", file=sys.stderr)
        sys.exit(1)

    output = notes_dir / "index.md"
    content = generate(notes_dir)
    output.write_text(content)
    count = content.count("\n- ")
    print(f"Generated {output} with {count} entries")
