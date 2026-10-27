"""ProperDocs hooks: metadata badge, collection nav, build-time generated listings.

Complete generated listings (per-collection dir-index pages and per-tag
generated tails) are materialized here at build time for the published site;
they are never committed (ADR 025). Agents use curated heads plus scoped rg.
Tag pages are the heads in kb/tags/ (ADR 089); a tail lists every member
across the participating collections.
"""

import os
import re
from functools import cache
from pathlib import Path

from properdocs.plugins import event_priority
from properdocs.structure.files import File, InclusionLevel

from commonplace.lib import index_directory, index_generated
from commonplace.lib.index_directory import UNPUBLISHED_COLLECTIONS
from commonplace.lib.project_paths import VALIDATION_IGNORE_MARKER

# Report retained/ pages are published, except subtrees carrying the
# validation-ignore marker: exact captures and trial bundles are data, not
# pages whose links or types the KB vouches for. properdocs.yml excludes the
# local state/ and cache/ areas.
REPORTS = "reports"

# Published collections left out of the main menu; their pages still build.
HIDDEN_FROM_NAV = frozenset({"agent-memory-systems", "types"})

# The "Agentic Systems" menu entry gathers these two collections into one
# dropdown: the analyses list, each landed lens, then the authored accounts.
AGENTIC_SYSTEMS_GROUP = ("agentic-system-analyses", "agentic-systems")

# Lens directories under agentic-systems/comparisons/ hold cross-system pages
# for one analyst member; each gets a build-time list of that member across
# the current analyses. A lens joins the menu when its README.md lands.
LENS_ROOT = Path("agentic-systems/comparisons")
LENSES = {"runtime": "Runtime", "memory": "Memory", "epistemic": "Epistemic", "workflow": "Workflow"}
# Extra members a lens list links beside its own member.
LENS_COMPANIONS = {"memory": {"memory-profile": "Profile"}}

# Directories that received a virtual dir-index page in on_files, so
# on_page_markdown can link each collection README to its full listing.
_generated_index_dirs: set[Path] = set()


def on_config(config):
    """Generate top-level nav from kb/<collection>/README.md files.

    Public directories directly under docs_dir with a README.md become
    top-nav entries. Tags comes first, followed by alphabetical discovery;
    the operational mailbox and HIDDEN_FROM_NAV are omitted, and the two
    agentic-systems collections share one dropdown with the landed lenses.
    Fixed Home and GitHub entries bracket the auto-discovered list.
    """
    _tag_space.cache_clear()
    docs_dir = Path(config["docs_dir"])
    collection_entries = []
    grouped = False
    for child in sorted(
        docs_dir.iterdir(), key=lambda path: (path.name != "tags", path.name)
    ):
        if not child.is_dir() or child.name.startswith("."):
            continue
        if child.name in UNPUBLISHED_COLLECTIONS | HIDDEN_FROM_NAV:
            continue
        readme = child / "README.md"
        if not readme.exists():
            continue
        if child.name in AGENTIC_SYSTEMS_GROUP:
            if not grouped:
                collection_entries.append(_agentic_systems_entry(docs_dir))
                grouped = True
            continue
        label = child.name.replace("-", " ").title()
        collection_entries.append({label: readme.relative_to(docs_dir).as_posix()})

    # TODO: read external links (GitHub, etc.) from properdocs.yml
    # so consuming projects don't have to fork this hook to change them.
    config["nav"] = [
        {"Home": "index.md"},
        *collection_entries,
        {"GitHub": "https://github.com/zby/commonplace"},
    ]
    return config


def _agentic_systems_entry(docs_dir: Path) -> dict:
    entries = []
    if (docs_dir / "agentic-system-analyses" / "README.md").exists():
        entries.append({"Analyses": "agentic-system-analyses/current-analyses.md"})
    for lens, label in LENSES.items():
        if (docs_dir / LENS_ROOT / lens / "README.md").exists():
            entries.append({label: (LENS_ROOT / lens / "README.md").as_posix()})
    if (docs_dir / "agentic-systems" / "README.md").exists():
        entries.append({"Authored accounts": "agentic-systems/README.md"})
    return {"Agentic Systems": entries}


def _cell(value) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def _relative_link(target: Path, start: Path) -> str:
    """A Markdown link target, with "/" on every platform."""
    return Path(os.path.relpath(target, start)).as_posix()


def _lens_listing(lens: str, analyses, lens_dir: Path) -> str:
    companions = LENS_COMPANIONS.get(lens, {})
    header = ["System", f"{LENSES[lens]} account", *companions.values()]
    lines = [f"# {LENSES[lens]}: current analyses", "",
             "| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    for analysis in analyses:
        member = analysis.roles[lens]
        href = _relative_link(member.path, lens_dir)
        cells = [_cell(analysis.overview.frontmatter["system"]),
                 f"[{_cell(member.frontmatter.get('description', lens))}]({href})"]
        cells += [f"[{label.lower()}]({_relative_link(analysis.roles[role].path, lens_dir)})"
                  for role, label in companions.items()]
        lines.append("| " + " | ".join(cells) + " |")
    if not analyses:
        lines += ["", "No current analyses. Regeneration is separately commissioned."]
    return "\n".join(lines) + "\n"


def _replace_generated(files, config, src_uri: str, content: str) -> None:
    for existing in list(files):
        if existing.src_uri == src_uri:
            files.remove(existing)
    files.append(File.generated(config, src_uri, content=content, inclusion=InclusionLevel.INCLUDED))


# Redirect plugins snapshot documentation pages at their default-priority
# on_files event. Materialize virtual pages first so their old URLs get HTML
# redirects too, rather than a warning and no redirect file at post-build.
@event_priority(50)
def on_files(files, config):
    """Add per-collection dir-index pages as build-time virtual files.

    Content comes from the same lib generation the retired
    commonplace-refresh-indexes command used, but stays in memory: the pages
    exist only in the built site. A stale on-disk dir-index.md (gitignored
    leftover) is replaced by the generated version.
    """
    _generated_index_dirs.clear()
    _exclude_marked_reports(files, Path(config["docs_dir"]).resolve())
    docs_dir = Path(config["docs_dir"]).resolve()
    root = docs_dir.parent
    published_paths = {
        Path(file.abs_src_path).resolve()
        for file in files.documentation_pages()
        if file.abs_src_path is not None
    }

    pages = index_directory.collect_site_index_pages(
        root, include=lambda path: path.resolve() in published_paths,
    )
    for output_path, content in pages:
        src_uri = output_path.relative_to(docs_dir).as_posix()
        stale = files.get_file_from_path(src_uri)
        if stale is not None:
            files.remove(stale)
        files.append(
            File.generated(
                config,
                src_uri,
                content=content,
                inclusion=InclusionLevel.INCLUDED,
            )
        )
        _generated_index_dirs.add(output_path.parent)

    collection = docs_dir / "agentic-system-analyses"
    if collection.is_dir():
        from commonplace.lib.agentic_analysis.analyses import current_analyses
        analyses = current_analyses(root)
        lines = ["# Current agentic-system analyses", "",
                 "| System | Description | Boundary | Run | Date | Evidence |", "|---|---|---|---|---|---|"]
        for analysis in analyses:
            data = analysis.overview.frontmatter
            href = analysis.overview.path.relative_to(collection).as_posix()
            values = [f"[{_cell(data['system'])}]({href})", *[_cell(data[key]) for key in
                      ("description", "reviewed-boundary", "run-id", "run-date", "evidence-tier")]]
            lines.append("| " + " | ".join(values) + " |")
        if len(lines) == 4:
            lines += ["", "No current analyses. Regeneration is separately commissioned."]
        _replace_generated(files, config, "agentic-system-analyses/current-analyses.md", "\n".join(lines) + "\n")
        for lens in LENSES:
            lens_dir = docs_dir / LENS_ROOT / lens
            if (lens_dir / "README.md").exists():
                _replace_generated(files, config, (LENS_ROOT / lens / "systems.md").as_posix(),
                                   _lens_listing(lens, analyses, lens_dir.resolve()))
    return files


def _exclude_marked_reports(files, docs_dir: Path) -> None:
    reports = docs_dir / REPORTS
    marked: dict[Path, bool] = {}

    def is_marked(directory: Path) -> bool:
        if directory not in marked:
            marked[directory] = (directory / VALIDATION_IGNORE_MARKER).exists() or (
                directory != reports and is_marked(directory.parent))
        return marked[directory]

    for file in files:
        if file.abs_src_path is None or not file.src_uri.startswith(f"{REPORTS}/"):
            continue
        if is_marked(Path(file.abs_src_path).resolve().parent):
            file.inclusion = InclusionLevel.EXCLUDED


@cache
def _tag_space(root: Path) -> index_generated.TagSpace:
    """Per-build cache of one tag-space scan."""
    return index_generated.collect_tag_space(root)


def _root_for(config) -> Path | None:
    if config is None:
        return None
    return Path(config["docs_dir"]).resolve().parent


def _is_head(page_path: Path, meta: dict, root: Path) -> bool:
    return (
        meta.get("type") == index_generated.TAG_README_TYPE
        and page_path.resolve().parent == index_generated.tags_collection(root).resolve()
        and index_generated.tag_for_head(page_path) is not None
    )


def _append_generated_tail(markdown: str, page, config) -> str:
    """Append the generated member listing to a tag head at build time."""
    meta = page.meta or {}
    root = _root_for(config)
    if root is None or page.file.abs_src_path is None:
        return markdown
    page_path = Path(page.file.abs_src_path)
    if not _is_head(page_path, meta, root):
        return markdown

    section = index_generated.generated_section_for_head(
        page_path, curated_text=markdown, tag_space=_tag_space(root)
    )
    # A complete-marked head curates every member, leaving the generated
    # section as a bare heading — skip it rather than render an empty shell.
    if not section or "\n- " not in section:
        return markdown
    return markdown.rstrip("\n") + "\n\n" + section


def _append_full_listing_link(markdown: str, page) -> str:
    """Link a collection README to its build-time dir-index sibling."""
    abs_src_path = page.file.abs_src_path
    if abs_src_path is None:  # generated virtual file
        return markdown
    page_path = Path(abs_src_path)
    if page_path.name != "README.md" or page_path.parent not in _generated_index_dirs:
        return markdown
    return (
        markdown.rstrip("\n")
        + "\n\n---\n\n[Complete file listing](./dir-index.md) *(generated at build time)*\n"
    )


def _tag_link(tag: str, note_dir: Path, root: Path | None) -> str:
    """Link a tag to its head when the head exists; otherwise plain text."""
    if root is not None:
        head = _tag_space(root).heads.get(tag)
        if head is not None:
            return f"[{tag}]({_relative_link(head, note_dir.resolve())})"
    return tag


def on_page_markdown(markdown: str, page, config=None, **kwargs) -> str:
    meta = page.meta or {}

    if meta:
        markdown = _append_generated_tail(markdown, page, config)
    markdown = _append_full_listing_link(markdown, page)
    if page.file.abs_src_path is not None:
        path = Path(page.file.abs_src_path)
        if path.name == "README.md" and path.parent.name == "agentic-system-analyses":
            markdown += "\n\n[Current analyses](./current-analyses.md) *(generated at build time)*\n"
        if path.name == "README.md" and path.parent.name in LENSES and path.parent.parent.name == LENS_ROOT.name:
            markdown += "\n\n[Current analyses](./systems.md) *(generated at build time)*\n"


    status = meta.get("status")
    user_verified = meta.get("user-verified") is True
    note_type = meta.get("type")
    tags = meta.get("tags", [])
    if not status and not user_verified and not note_type and not tags:
        return markdown

    parts = []
    if note_type:
        parts.append(f"**Type:** {note_type}")
    if status:
        parts.append(f"**Status:** {status}")
    if user_verified:
        parts.append("**User verified:** yes")

    if tags:
        note_dir = Path(page.file.abs_src_path).parent
        root = _root_for(config)
        parts.append(
            "**Tags:** " + ", ".join(_tag_link(tag, note_dir, root) for tag in tags)
        )

    badge_line = " · ".join(parts)

    # Insert after the first heading. A function replacement keeps "\" in page values literal.
    return re.sub(
        r"(^# .+\n)",
        lambda match: f"{match.group(1)}\n{badge_line}\n",
        markdown,
        count=1,
        flags=re.MULTILINE,
    )
