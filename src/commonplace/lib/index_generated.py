"""The tag space: heads, participating collections, membership, generated tails.

One KB has one tag namespace (ADR 089). Every tag head is
``kb/tags/<tag>-README.md``; the filename is the head's identity. Membership
ranges over the collections that ``kb/tags/COLLECTION.md`` declares as
participating, and nothing outside that set is read. Generated tails are
build-time materializations for the published site, never committed (ADR 025).
"""

from __future__ import annotations

import os
import re
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.lib.note_parser import ParsedDocument, parse_document
from commonplace.lib.project_paths import (
    is_collection_dir,
    is_proposal_archive,
    is_replaced_archive,
    iter_visible_markdown_files,
    kb_root,
)

FIELD_NAME = "tags"
MARKER = "<!-- generated -->"
TAG_README_TYPE = "types/tag-readme.md"
TAGS_COLLECTION_NAME = "tags"
PARTICIPATING_FIELD = "participating"
HEAD_SUFFIX = "-README.md"
GENERATED_HEADING = "## Other tagged notes"
URL_SCHEME_RE = re.compile(r"^[a-z][a-z0-9+.-]*:", re.IGNORECASE)

Entry = tuple[Path, str, str]
LoadDocument = Callable[[Path], ParsedDocument | None]


def tags_collection(root: Path) -> Path:
    """Return the tag collection directory for a project root."""
    return kb_root(root) / TAGS_COLLECTION_NAME


def head_path(root: Path, tag: str) -> Path:
    """Return the canonical head path for a tag."""
    return tags_collection(root) / f"{tag}{HEAD_SUFFIX}"


def tag_for_head(path: Path) -> str | None:
    """Return the tag a head file names, or None for any other file.

    The collection landing ``README.md`` is not a head.
    """
    name = path.name
    if not name.endswith(HEAD_SUFFIX) or name == HEAD_SUFFIX[1:]:
        return None
    tag = name[: -len(HEAD_SUFFIX)]
    return tag or None


@dataclass(frozen=True)
class TagSpace:
    """One scan of a KB's tag space."""

    participating: tuple[Path, ...]
    notes_by_tag: dict[str, list[Entry]]
    heads: dict[str, Path]
    declaration_error: str | None

    @property
    def tags_in_use(self) -> set[str]:
        return set(self.notes_by_tag)

    def is_participating(self, path: Path) -> bool:
        """Return True when path is a membership candidate: inside a
        participating collection and not in an excluded subtree."""
        resolved = path.resolve()
        for collection in self.participating:
            if resolved == collection or collection in resolved.parents:
                return _is_member_candidate(resolved, collection)
        return False


def _default_load_document(path: Path) -> ParsedDocument | None:
    document, _error = parse_document(path.read_text(encoding="utf-8"))
    return document


def read_participating(
    root: Path, *, load_document: LoadDocument | None = None
) -> tuple[tuple[Path, ...], str | None]:
    """Read the participating collections declared by ``kb/tags/COLLECTION.md``.

    Returns the resolved collection directories and an error message when the
    declaration is missing or names something that is not a collection. An
    undeclared tag space has no members: nothing is inferred from the tree.
    """
    collection = tags_collection(root).resolve()
    contract = collection / "COLLECTION.md"
    if not contract.is_file():
        return (), f"tag space undeclared: {contract} does not exist (run commonplace-init)"

    if load_document is None:
        data = frontmatter.parse(contract.read_text(encoding="utf-8")).data
    else:
        document = load_document(contract)
        data = (document.frontmatter if document is not None else None) or {}

    declared = data.get(PARTICIPATING_FIELD)
    if not isinstance(declared, list) or not all(isinstance(item, str) for item in declared):
        return (), (
            f"tag space undeclared: {contract} has no `{PARTICIPATING_FIELD}:` list "
            "of collection names"
        )

    boundary = kb_root(root).resolve()
    participating: list[Path] = []
    problems: list[str] = []
    for name in declared:
        candidate = (boundary / name).resolve()
        if name == TAGS_COLLECTION_NAME:
            problems.append(f"`{name}` holds the heads and cannot participate")
        elif boundary not in candidate.parents or not is_collection_dir(candidate):
            problems.append(f"`{name}` is not a collection under {boundary}")
        else:
            participating.append(candidate)
    error = None
    if problems:
        error = f"tag space declaration in {contract}: " + "; ".join(problems)
    return tuple(participating), error


def _is_member_candidate(path: Path, collection: Path) -> bool:
    """Files a participating collection contributes: not frozen archives,
    type definitions, collection internals, or the contract itself."""
    if is_replaced_archive(path) or is_proposal_archive(path):
        return False
    rel_parts = path.relative_to(collection).parts
    if "types" in rel_parts or ".collection" in rel_parts:
        return False
    return path.name != "COLLECTION.md"


def _scan_members(
    collection: Path, load_document: LoadDocument, by_tag: dict[str, list[Entry]]
) -> None:
    for path in sorted(iter_visible_markdown_files(collection)):
        if not _is_member_candidate(path, collection):
            continue
        document = load_document(path)
        if document is None:
            continue
        fm = document.frontmatter or {}
        tags = fm.get(FIELD_NAME)
        if not isinstance(tags, list):
            continue
        entry = (path, document.title, str(fm.get("description", "")))
        for tag in tags:
            if isinstance(tag, str):
                by_tag.setdefault(tag, []).append(entry)


def collect_heads(root: Path) -> dict[str, Path]:
    """Return every head in the tag collection, keyed by tag."""
    collection = tags_collection(root)
    if not collection.is_dir():
        return {}
    heads: dict[str, Path] = {}
    for path in sorted(collection.glob(f"*{HEAD_SUFFIX}")):
        tag = tag_for_head(path)
        if tag is not None:
            heads[tag] = path.resolve()
    return heads


def collect_tag_space(
    root: Path, *, load_document: LoadDocument | None = None
) -> TagSpace:
    """Scan the participating collections once for membership, and the tag
    collection for heads."""
    if load_document is None:
        load_document = _default_load_document
    participating, error = read_participating(root, load_document=load_document)
    by_tag: dict[str, list[Entry]] = {}
    for collection in participating:
        _scan_members(collection, load_document, by_tag)
    return TagSpace(participating, by_tag, collect_heads(root), error)


def extract_curated_links(curated_section: str) -> set[str]:
    """Extract link targets from the curated section above the marker."""
    return set(re.findall(r"\]\(([^)]+)\)", curated_section))


def _display_relpath(path: Path, index_dir: Path) -> str:
    relpath = Path(os.path.relpath(path, index_dir)).as_posix()
    if relpath != ".." and not relpath.startswith("../"):
        relpath = f"./{relpath}"
    return relpath


def _normalize_curated_link_target(target: str) -> str:
    bare_target = target.split("#", 1)[0]
    if not bare_target or bare_target.startswith("/") or URL_SCHEME_RE.match(bare_target):
        return bare_target

    normalized = Path(os.path.normpath(bare_target)).as_posix()
    if normalized != ".." and not normalized.startswith("../"):
        normalized = f"./{normalized}"
    return normalized


def build_generated_section(
    entries: list[Entry],
    index_dir: Path,
    heading: str,
    curated_links: set[str] | None = None,
) -> str:
    """Build a generated listing section, excluding already-curated notes."""
    lines = [f"{heading} {MARKER}", ""]
    normalized_curated_links = (
        {_normalize_curated_link_target(link) for link in curated_links}
        if curated_links
        else set()
    )

    for path, title, desc in sorted(entries, key=lambda x: x[1].lower()):
        relpath = _display_relpath(path, index_dir)
        if relpath in normalized_curated_links:
            continue
        entry = f"- [{title}]({relpath})"
        if desc:
            entry += f" - {desc}"
        lines.append(entry)

    lines.append("")
    return "\n".join(lines)


def generated_section_for_head(
    head: Path, *, curated_text: str, tag_space: TagSpace
) -> str | None:
    """Build the generated tail for one head, in memory.

    ``curated_text`` is the head's committed body; links already curated there
    are excluded from the listing. Returns None for a file that is not a head.
    """
    tag = tag_for_head(head)
    if tag is None:
        return None
    return build_generated_section(
        tag_space.notes_by_tag.get(tag, []),
        head.parent,
        GENERATED_HEADING,
        extract_curated_links(curated_text),
    )
