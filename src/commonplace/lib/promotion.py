"""Promotion candidate report generation."""

from __future__ import annotations

import os
from collections import defaultdict
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

from commonplace.lib import frontmatter as fm_mod
from commonplace.lib.note_parser import (
    extract_title,
    find_markdown_links,
    strip_frontmatter,
)
from commonplace.lib.project_paths import (
    kb_root,
    list_collection_validation_paths,
    resolve_collection,
)


@dataclass(frozen=True)
class PromotionReportResult:
    output: Path
    text_count: int
    invalid_count: int


def resolve_link(source: Path, target: str) -> Path | None:
    """Resolve a relative link target to an absolute path."""
    if target.startswith(("http://", "https://")):
        return None
    target = target.split("#")[0]
    if not target:
        return None
    return (source.parent / target).resolve()


def write_promotion_candidates_report(
    root: Path, collection: str,
) -> PromotionReportResult:
    """Rank candidates in an explicit collection, with a scope-specific report."""
    root = root.resolve()
    notes_dir = resolve_collection(collection, root)
    output = (
        kb_root(root) / "reports" / "cache" / "promotion-candidates"
        / notes_dir.relative_to(kb_root(root)) / "report.md"
    )

    def report_link(path: Path) -> str:
        return Path(os.path.relpath(path, output.parent)).as_posix()

    text_files: dict[Path, str] = {}
    invalid_frontmatter: dict[Path, tuple[str, ...]] = {}
    all_notes: dict[Path, dict] = {}

    for path in list_collection_validation_paths(notes_dir):
        if not path.is_file() or path.suffix != ".md":
            continue
        if path.name in ("index.md", "dir-index.md", "README.md"):
            continue

        abs_path = path.resolve()
        content = path.read_text(encoding="utf-8")
        if fm_mod.opens_frontmatter(content):
            parsed_frontmatter = fm_mod.parse(content)
            frontmatter = parsed_frontmatter.data
            if not parsed_frontmatter.ok:
                invalid_frontmatter[abs_path] = tuple(parsed_frontmatter.errors)
        else:
            frontmatter = None
        body = strip_frontmatter(content)
        title = extract_title(body)
        links = find_markdown_links(body)
        all_notes[abs_path] = {"fm": frontmatter, "title": title, "links": links, "rel": path}

        if frontmatter is None:
            text_files[abs_path] = title

    incoming_links: dict[Path, list[Path]] = defaultdict(list)
    for source_path, info in all_notes.items():
        for link in info["links"]:
            resolved = resolve_link(source_path, link)
            if resolved and resolved in all_notes:
                incoming_links[resolved].append(source_path)

    def rank(candidates: dict[Path, str]) -> list[tuple[Path, str, int, list[Path]]]:
        ranked = [
            (
                all_notes[path]["rel"].relative_to(notes_dir),
                title,
                len(incoming_links.get(path, [])),
                incoming_links.get(path, []),
            )
            for path, title in sorted(candidates.items())
        ]
        ranked.sort(key=lambda x: (-x[2], str(x[0])))
        return ranked

    def render_entries(entries: list[tuple[Path, str, int, list[Path]]]) -> list[str]:
        lines: list[str] = []
        for rel, title, count, sources in entries:
            source_list = ", ".join(
                f"[{all_notes[s]['title']}]({report_link(s)})"
                for s in sources[:3]
            )
            if len(sources) > 3:
                source_list += f" +{len(sources) - 3} more"
            lines.append(f"- [{title}]({report_link(notes_dir / rel)}) - **{count} links in**")
            if source_list:
                lines.append(f"  Sources: {source_list}")
            lines.append("")
        return lines

    text_with_links = rank(text_files)
    lines = [
        f"# Unstructured Text Candidates - {datetime.now(UTC).astimezone().date()}",
        "",
        f"Collection: `{notes_dir.relative_to(root).as_posix()}`",
        "",
        f"Unstructured text files: {len(text_files)}",
        "",
    ]

    lines.extend(["## Text -> Note", ""])
    if text_with_links:
        lines.extend(render_entries(text_with_links))
    else:
        lines.extend(["No text files found.", ""])

    lines.extend(["## Invalid frontmatter", ""])
    if invalid_frontmatter:
        for path, errors in sorted(invalid_frontmatter.items()):
            title = all_notes[path]["title"]
            lines.append(f"- [{title}]({report_link(path)})")
            for error in errors:
                diagnostic = " ".join(error.split())
                lines.append(f"  - {diagnostic}")
            lines.append("")
    else:
        lines.extend(["No invalid frontmatter found.", ""])

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")
    return PromotionReportResult(output, len(text_files), len(invalid_frontmatter))
