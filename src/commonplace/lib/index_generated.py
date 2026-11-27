"""Shared tag heads, exact membership and collection-grouped site listings."""

from __future__ import annotations

import os
from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from commonplace.lib.note_parser import parse_document
from commonplace.lib.project_paths import (
    VALIDATION_IGNORE_MARKER,
    is_collection_dir,
    is_proposal_archive,
    is_replaced_archive,
    kb_root,
    walk_visible,
)

TAG_README_TYPE = "types/tag-readme.md"
HEAD_SUFFIX = "-README.md"
# Heads and type definitions are metadata; workflow state is never a member source.
EXCLUDED_COLLECTIONS = {"tags", "types", "workflow-state"}
SOURCE_SNAPSHOTS = ".snapshots"
Entry = tuple[Path, str, str]


def tags_collection(root: Path) -> Path:
    return kb_root(root) / "tags"


def head_path(root: Path, tag: str) -> Path:
    return tags_collection(root) / f"{tag}{HEAD_SUFFIX}"


def tag_for_head(path: Path) -> str | None:
    """Return the tag named by a head filename, never the collection landing."""
    return (
        (path.name.removesuffix(HEAD_SUFFIX) or None)
        if path.name.endswith(HEAD_SUFFIX)
        else None
    )


@dataclass(frozen=True)
class TagCatalog:
    collections: tuple[Path, ...]
    heads: dict[str, Path]

    def is_member_candidate(self, path: Path) -> bool:
        """Check a single target without enumerating any collection's files."""
        path = path.resolve()
        for collection in self.collections:
            if not path.is_relative_to(collection):
                continue
            parts = path.relative_to(collection).parts
            if not parts or path.suffix != ".md" or path.name == "COLLECTION.md":
                return False
            if any(p.startswith(".") or p == "types" for p in parts):
                return False
            if is_replaced_archive(path) or is_proposal_archive(path):
                return False
            current = path.parent
            while current.is_relative_to(collection):
                if (current / VALIDATION_IGNORE_MARKER).exists() or (
                    current / ".git"
                ).exists():
                    return False
                current = current.parent
            return True
        return False


@dataclass(frozen=True)
class TagSpace(TagCatalog):
    notes_by_tag: dict[str, list[Entry]]


def collect_tag_catalog(root: Path) -> TagCatalog:
    """Inspect only immediate collection roots and head filenames."""
    kb = kb_root(root).resolve()
    collections = (
        tuple(
            sorted(
                p
                for p in kb.iterdir()
                if p.name not in EXCLUDED_COLLECTIONS
                and not p.name.startswith(".")
                and not p.is_symlink()
                and not (p / ".git").exists()
                and is_collection_dir(p)
            )
        )
        if kb.is_dir()
        else ()
    )
    heads = {
        tag: path.resolve()
        for path in tags_collection(root).glob(f"*{HEAD_SUFFIX}")
        if path.is_file() and (tag := tag_for_head(path)) is not None
    }
    return TagCatalog(collections, heads)


def collect_tag_space(root: Path) -> TagSpace:
    """Scan eligible collections once. Prune non-member trees before reading files."""
    catalog = collect_tag_catalog(root)
    by_tag: dict[str, list[Entry]] = defaultdict(list)
    for collection in catalog.collections:
        excluded = {"types"}
        if collection.name == "sources":
            excluded.add(SOURCE_SNAPSHOTS)
        for directory, dirs, files in walk_visible(
            collection, exclude_dir_names=frozenset(excluded)
        ):
            if VALIDATION_IGNORE_MARKER in files:
                dirs.clear()
                continue
            if directory.name == "proposals" and "archive" in dirs:
                dirs.remove("archive")
            for name in files:
                path = directory / name
                if (
                    not name.endswith(".md")
                    or name.startswith(".")
                    or name == "COLLECTION.md"
                    or is_replaced_archive(path)
                    or path.is_symlink()
                ):
                    continue
                document, _ = parse_document(path.read_text(encoding="utf-8"))
                fm = document.frontmatter if document else None
                if (
                    not fm
                    or not isinstance(fm.get("tags"), list)
                    or fm.get("type") == "types/snapshot.md"
                ):
                    continue
                entry = (path, document.title, str(fm.get("description", "")))
                for tag in dict.fromkeys(t for t in fm["tags"] if isinstance(t, str)):
                    by_tag[tag].append(entry)
    return TagSpace(catalog.collections, catalog.heads, dict(by_tag))


def tag_members_page(
    tag: str, *, tag_space: TagSpace, published: Callable[[Path], bool]
) -> tuple[str, str]:
    """Return the head's navigation line and its complete, collection-grouped sibling."""
    head = tag_space.heads[tag]
    entries = tag_space.notes_by_tag.get(tag, [])
    kb = head.parent.parent
    groups: dict[str, list[Entry]] = defaultdict(list)
    for entry in entries:
        groups[entry[0].relative_to(kb).parts[0]].append(entry)
    preferred = ("theory", "articles", "notes", "agentic-systems", "agentic-system-analyses",
                 "reference", "instructions", "sources", "agent-memory-systems")
    order = [name for name in preferred if name in groups] + sorted(groups.keys() - set(preferred))
    link = f"[All {len(entries)} tagged artifacts](./{tag}-members.md)"
    if order:
        link += " — " + ", ".join(f"{len(groups[name])} {name}" for name in order)
    lines = [f"# {tag}: tagged artifacts", "", f"[Back to the {tag} guide](./{head.name})", ""]
    if order:
        lines.append(" · ".join(f"[{name}](#{name})" for name in order))
    else:
        lines.append("No tagged artifacts.")
    for collection in order:
        lines.extend(["", f"## {collection}", ""])
        for path, title, desc in sorted(groups[collection], key=lambda e: (e[1].casefold(), e[0])):
            if published(path):
                label = f"[{title}]({Path(os.path.relpath(path, head.parent)).as_posix()})"
            else:
                label = f"{title} (`{path.relative_to(kb).as_posix()}`)"
            lines.append(f"- {label}" + (f" - {desc}" if desc else ""))
    return link + " *(generated at build time)*", "\n".join(lines) + "\n"
