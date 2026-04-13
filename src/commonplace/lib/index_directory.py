"""Generate directory index pages from markdown frontmatter."""

from __future__ import annotations

from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.lib.note_parser import extract_title, strip_frontmatter
from commonplace.lib.project_paths import is_type_definition_content


def entry_sort_key(entry: tuple[str, str, str, str]) -> tuple[str, str]:
    """Sort by visible link text first, then by path for deterministic ties."""
    rel_path, title, _desc, _note_type = entry
    return (title.casefold(), rel_path.casefold())


def generate(notes_dir: Path) -> str:
    """Generate index.md content for a directory."""
    output = notes_dir / "index.md"
    entries: list[tuple[str, str, str, str]] = []

    for path in sorted(notes_dir.rglob("*.md")):
        if path == output or path.name == "README.md":
            continue
        if is_type_definition_content(path, notes_dir):
            continue

        content = path.read_text(encoding="utf-8")
        fm = frontmatter.parse(content).data
        title = extract_title(strip_frontmatter(content))
        desc = fm.get("description", "")
        note_type = fm.get("type", "")
        rel = path.relative_to(notes_dir)

        entries.append((str(rel), title, desc, note_type))

    entries.sort(key=entry_sort_key)

    lines = [
        "---",
        "description: Auto-generated directory - run commonplace-refresh-indexes to rebuild",
        "type: index",
        "index_source: directory",
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
            parts.append(f"- {desc}")
        lines.append(" ".join(parts))

    lines.append("")
    return "\n".join(lines)


def write_index(notes_dir: Path) -> tuple[Path, int]:
    """Generate and write index.md for a directory."""
    output = notes_dir / "index.md"
    content = generate(notes_dir)
    output.write_text(content, encoding="utf-8")
    count = content.count("\n- ")
    return output, count
