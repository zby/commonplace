"""Promotion candidate report generation."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from commonplace.lib import frontmatter as fm_mod
from commonplace.lib.note_parser import extract_title, find_markdown_links, strip_frontmatter
from commonplace.lib.project_paths import list_collection_note_paths


@dataclass(frozen=True)
class PromotionReportResult:
    output: Path
    text_count: int
    seedling_count: int


def resolve_link(source: Path, target: str) -> Path | None:
    """Resolve a relative link target to an absolute path."""
    if target.startswith("http://") or target.startswith("https://"):
        return None
    target = target.split("#")[0]
    if not target:
        return None
    return (source.parent / target).resolve()


def write_promotion_candidates_report(root: Path) -> PromotionReportResult:
    """Write the promotion candidates report for kb/notes/."""
    notes_dir = root / "kb" / "notes"
    reports_dir = root / "kb" / "reports"
    if not notes_dir.is_dir():
        raise FileNotFoundError(f"Not a directory: {notes_dir}")

    text_files: dict[Path, str] = {}
    seedlings: dict[Path, str] = {}
    all_notes: dict[Path, dict] = {}

    for path in list_collection_note_paths(notes_dir):
        if path.name in ("index.md", "README.md"):
            continue

        abs_path = path.resolve()
        content = path.read_text(encoding="utf-8")
        frontmatter = fm_mod.parse(content).data if content.startswith("---\n") else None
        body = strip_frontmatter(content)
        title = extract_title(body)
        links = find_markdown_links(body)
        all_notes[abs_path] = {"fm": frontmatter, "title": title, "links": links, "rel": path}

        if frontmatter is None:
            text_files[abs_path] = title
        elif frontmatter.get("status") == "seedling":
            seedlings[abs_path] = title

    incoming_links: dict[Path, list[Path]] = defaultdict(list)
    for source_path, info in all_notes.items():
        for link in info["links"]:
            resolved = resolve_link(source_path, link)
            if resolved and resolved in all_notes:
                incoming_links[resolved].append(source_path)

    text_with_links = []
    for path, title in sorted(text_files.items()):
        sources = incoming_links.get(path, [])
        real_sources = [s for s in sources if all_notes[s]["rel"].name != "index.md"]
        rel = all_notes[path]["rel"].relative_to(notes_dir)
        text_with_links.append((rel, title, len(real_sources), real_sources))
    text_with_links.sort(key=lambda x: (-x[2], str(x[0])))

    seedling_ranked = []
    for path, title in sorted(seedlings.items()):
        sources = incoming_links.get(path, [])
        real_sources = [s for s in sources if all_notes[s]["rel"].name != "index.md"]
        rel = all_notes[path]["rel"].relative_to(notes_dir)
        seedling_ranked.append((rel, title, len(real_sources), real_sources))
    seedling_ranked.sort(key=lambda x: (-x[2], str(x[0])))

    lines = [
        f"# Promotion Candidates - {date.today()}",
        "",
        f"Text files: {len(text_files)} | Seedlings: {len(seedlings)}",
        "",
    ]

    lines.extend(["## Text -> Note", ""])
    if text_with_links:
        for rel, title, count, sources in text_with_links:
            source_list = ", ".join(
                f"[{all_notes[s]['title']}](../notes/{all_notes[s]['rel'].relative_to(notes_dir)})"
                for s in sources[:3]
            )
            if len(sources) > 3:
                source_list += f" +{len(sources) - 3} more"
            lines.append(f"- [{title}](../notes/{rel}) - **{count} links in**")
            if source_list:
                lines.append(f"  Sources: {source_list}")
            lines.append("")
    else:
        lines.extend(["No text files found.", ""])

    lines.extend(["## Seedling -> Current (top 20 by incoming links)", ""])
    top_seedlings = seedling_ranked[:20]
    if top_seedlings:
        for rel, title, count, sources in top_seedlings:
            source_list = ", ".join(
                f"[{all_notes[s]['title']}](../notes/{all_notes[s]['rel'].relative_to(notes_dir)})"
                for s in sources[:3]
            )
            if len(sources) > 3:
                source_list += f" +{len(sources) - 3} more"
            lines.append(f"- [{title}](../notes/{rel}) - **{count} links in**")
            if source_list:
                lines.append(f"  Sources: {source_list}")
            lines.append("")
    else:
        lines.extend(["No seedling notes found.", ""])
    lines.append("")

    orphan_seedlings = [item for item in seedling_ranked if item[2] == 0]
    if orphan_seedlings:
        lines.extend([f"## Orphan Seedlings ({len(orphan_seedlings)} with zero incoming links)", ""])
        for rel, title, _, _ in orphan_seedlings:
            lines.append(f"- [{title}](../notes/{rel})")
        lines.append("")

    output = reports_dir / "promotion-candidates.md"
    reports_dir.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")
    return PromotionReportResult(output, len(text_files), len(seedlings))
