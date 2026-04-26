"""Generate directory index pages from markdown frontmatter."""

from __future__ import annotations

from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.lib.note_parser import extract_title, strip_frontmatter
from commonplace.lib.project_paths import (
    is_replaced_archive,
    is_type_definition_content,
)
from commonplace.lib.project_paths import is_git_ignored, iter_unignored_markdown_files


SKIP_DIR_NAMES = {"types"}
INDEX_TYPE = "kb/types/index.md"


def entry_sort_key(entry: tuple[str, str, str, str]) -> tuple[str, str]:
    """Sort by visible link text first, then by path for deterministic ties."""
    rel_path, title, _desc, _note_type = entry
    return (title.casefold(), rel_path.casefold())


def _display_type(note_type: str) -> str:
    """Display path-valued types compactly in generated directory indexes."""
    if note_type.endswith(".md") and (
        note_type.startswith("kb/")
        or note_type.startswith("./")
        or note_type.startswith("../")
    ):
        return Path(note_type).stem
    return note_type


def _has_indexable_content(directory: Path, *, ignore_root: Path | None = None) -> bool:
    """True if the directory or any descendant holds an indexable .md file.

    Excludes README.md (curated landing) and dir-index.md (the generated index
    itself), and skips type-definition directories. Used to decide whether a
    subdirectory deserves its own dir-index.md.
    """
    for path in iter_unignored_markdown_files(directory, ignore_root=ignore_root):
        if path.name in ("README.md", "dir-index.md"):
            continue
        if is_replaced_archive(path):
            continue
        if is_type_definition_content(path, directory):
            continue
        if any(part in SKIP_DIR_NAMES for part in path.relative_to(directory).parts):
            continue
        return True
    return False


def _should_skip_subdir(subdir: Path, *, ignore_root: Path | None = None) -> bool:
    if subdir.name.startswith("."):
        return True
    if subdir.name in SKIP_DIR_NAMES:
        return True
    if is_git_ignored(subdir, ignore_root):
        return True
    return not _has_indexable_content(subdir, ignore_root=ignore_root)


def _subdir_link_target(subdir: Path, *, ignore_root: Path | None = None) -> str:
    """Pick the best landing inside `subdir` to link from a parent dir-index.

    Prefers dir-index.md, then README.md, then the sole `.md` file when the
    subdir contains exactly one (catches kb/instructions/cp-skill-*/SKILL.md
    and similar single-doc subdirs), then a bare directory URL.
    """
    dir_index = subdir / "dir-index.md"
    readme = subdir / "README.md"
    if dir_index.is_file() and not is_git_ignored(dir_index, ignore_root):
        return f"./{subdir.name}/dir-index.md"
    if readme.is_file() and not is_git_ignored(readme, ignore_root):
        return f"./{subdir.name}/README.md"
    md_files = [
        p
        for p in subdir.iterdir()
        if p.is_file()
        and p.suffix == ".md"
        and not is_replaced_archive(p)
        and not is_git_ignored(p, ignore_root)
    ]
    if len(md_files) == 1:
        return f"./{subdir.name}/{md_files[0].name}"
    return f"./{subdir.name}/"


def generate(
    notes_dir: Path,
    *,
    parent_link: str,
    ignore_root: Path | None = None,
) -> str:
    """Generate dir-index.md content for a single directory level.

    Lists files directly in `notes_dir` plus a row per qualifying subdirectory.
    `parent_link` is rendered as the back-link at the top of the page.
    """
    output = notes_dir / "dir-index.md"
    file_entries: list[tuple[str, str, str, str]] = []
    subdirs: list[Path] = []

    for path in sorted(notes_dir.iterdir()):
        if path.is_dir():
            if _should_skip_subdir(path, ignore_root=ignore_root):
                continue
            subdirs.append(path)
            continue
        if is_git_ignored(path, ignore_root):
            continue
        if path.suffix != ".md":
            continue
        if path == output or path.name == "README.md":
            continue
        if is_replaced_archive(path):
            continue
        if is_type_definition_content(path, notes_dir):
            continue

        content = path.read_text(encoding="utf-8")
        fm = frontmatter.parse(content).data
        title = extract_title(strip_frontmatter(content))
        desc = fm.get("description", "")
        note_type = fm.get("type", "")
        rel = path.relative_to(notes_dir)

        file_entries.append((str(rel), title, desc, note_type))

    file_entries.sort(key=entry_sort_key)

    lines = [
        "---",
        "description: Auto-generated directory - run commonplace-refresh-indexes to rebuild",
        f"type: {INDEX_TYPE}",
        "index_source: directory",
        "---",
        "",
        f"# {notes_dir.name.replace('-', ' ').title()} Directory",
        "",
        f"← [Parent]({parent_link})",
        "",
    ]

    if subdirs:
        lines.append("## Subdirectories")
        lines.append("")
        for subdir in subdirs:
            target = _subdir_link_target(subdir, ignore_root=ignore_root)
            lines.append(f"- [{subdir.name}/]({target})")
        lines.append("")

    if file_entries:
        if subdirs:
            lines.append("## Files")
            lines.append("")
        for rel, title, desc, note_type in file_entries:
            parts = [f"- [{title}](./{rel})"]
            if note_type:
                parts.append(f"*({_display_type(note_type)})*")
            if desc:
                parts.append(f"- {desc}")
            lines.append(" ".join(parts))
        lines.append("")

    return "\n".join(lines)


def write_index(
    notes_dir: Path,
    *,
    is_root: bool = True,
    max_depth: int | None = None,
    _depth: int = 0,
    ignore_root: Path | None = None,
) -> tuple[Path, int]:
    """Generate and write dir-index.md for `notes_dir`, recursing into subdirs.

    `is_root=True` indicates a collection root, in which case the parent link
    points at the kb-level homepage (`../index.md`). For nested levels the
    parent link points at the parent dir-index.

    `max_depth` caps recursion. None means recurse unconditionally; 1 means
    only generate the dir-index at this level (no nested dir-indexes). When
    recursion is capped, any stale dir-index.md files in skipped descendants
    are removed so the parent's subdir links cleanly fall back to README.md
    or a bare directory URL.
    """
    resolved_ignore_root = (ignore_root or notes_dir).resolve()
    will_recurse = max_depth is None or _depth + 1 < max_depth

    for subdir in sorted(notes_dir.iterdir()):
        if not subdir.is_dir() or _should_skip_subdir(
            subdir,
            ignore_root=resolved_ignore_root,
        ):
            continue
        if will_recurse:
            write_index(
                subdir,
                is_root=False,
                max_depth=max_depth,
                _depth=_depth + 1,
                ignore_root=resolved_ignore_root,
            )
        else:
            for stale in iter_unignored_markdown_files(
                subdir,
                ignore_root=resolved_ignore_root,
            ):
                if stale.name != "dir-index.md":
                    continue
                stale.unlink()

    parent_link = "../index.md" if is_root else "../dir-index.md"
    content = generate(
        notes_dir,
        parent_link=parent_link,
        ignore_root=resolved_ignore_root,
    )
    output = notes_dir / "dir-index.md"
    output.write_text(content, encoding="utf-8")
    count = content.count("\n- ")

    return output, count
