"""Source-conformance review pairs derived from an artifact's ingest links.

The virtual ``source`` lens pairs a selected Markdown artifact with each direct
``kb/sources/<slug>.ingest.md`` file it links. The ingest path is the persisted
criterion identity and ``source/<slug>`` is the public criterion id. Repeated
links and URL fragments do not create additional pairs.
"""

from __future__ import annotations

import re
from pathlib import Path, PurePosixPath

from commonplace.lib import frontmatter
from commonplace.lib.note_parser import find_markdown_links_with_text
from commonplace.lib.project_paths import kb_root

SOURCE_CONFORMANCE_LENS = "source"
SOURCE_INGEST_ROOT = PurePosixPath("kb/sources")
INGEST_SUFFIX = ".ingest.md"
URL_SCHEME_RE = re.compile(r"^[a-z]+://", re.IGNORECASE)


def is_source_conformance_request(arg: str) -> bool:
    """True when a request names the virtual source-conformance lens."""
    arg = arg.strip()
    return arg == SOURCE_CONFORMANCE_LENS or arg.startswith(f"{SOURCE_CONFORMANCE_LENS}/")


def is_source_ingest_criterion_path(criterion_path: str) -> bool:
    """True for a direct tracked ingest path under ``kb/sources/``."""
    path = PurePosixPath(criterion_path)
    return (
        len(path.parts) == 3
        and path.parent == SOURCE_INGEST_ROOT
        and path.name.endswith(INGEST_SUFFIX)
        and len(path.name) > len(INGEST_SUFFIX)
    )


def source_criterion_id_for_path(criterion_path: str) -> str:
    """Return the virtual ``source/<slug>`` id for an ingest criterion path."""
    if not is_source_ingest_criterion_path(criterion_path):
        raise ValueError(f"not a source ingest criterion path: {criterion_path}")
    name = PurePosixPath(criterion_path).name
    return f"{SOURCE_CONFORMANCE_LENS}/{name.removesuffix(INGEST_SUFFIX)}"


def resolve_source_criterion_id(repo_root: Path, criterion_id: str) -> str:
    """Resolve one ``source/<slug>`` id to its tracked ingest path.

    Bare ``source`` is derivational and therefore has no single path; the
    selector expands it only after an artifact scope has been chosen.
    """
    raw = criterion_id.strip()
    prefix = f"{SOURCE_CONFORMANCE_LENS}/"
    if raw == SOURCE_CONFORMANCE_LENS:
        raise ValueError("source requires an artifact scope; request source/<slug> for one concrete criterion")
    if not raw.startswith(prefix):
        raise ValueError(f"invalid source criterion id: {criterion_id}")
    slug = raw.removeprefix(prefix)
    if not slug or "/" in slug or slug in {".", ".."} or slug.endswith(INGEST_SUFFIX):
        raise ValueError(f"invalid source criterion id: {criterion_id}")
    repo_root_resolved = repo_root.resolve()
    ingest_abs = kb_root(repo_root_resolved) / "sources" / f"{slug}{INGEST_SUFFIX}"
    ingest_path = ingest_abs.relative_to(repo_root_resolved).as_posix()
    if not is_source_ingest_criterion_path(ingest_path):
        raise ValueError(f"invalid source criterion id: {criterion_id}")
    if not ingest_abs.is_file():
        raise FileNotFoundError(f"source ingest not found for criterion id: {criterion_id}")
    return ingest_path


def note_source_ingest_paths(repo_root: Path, note_abs: Path) -> list[str]:
    """Return deduplicated ingest paths resolved from one artifact's links."""
    note_text = note_abs.read_text(encoding="utf-8")
    note_body = frontmatter.strip(note_text).lstrip("\n")
    repo_root_resolved = repo_root.resolve()
    found: list[str] = []
    seen: set[str] = set()

    for _link_text, raw_target in find_markdown_links_with_text(note_body):
        if URL_SCHEME_RE.match(raw_target) or raw_target.startswith("#"):
            continue
        bare_target = raw_target.split("#", 1)[0]
        if not bare_target or not bare_target.endswith(".md"):
            continue
        candidate = (note_abs.parent / bare_target).resolve()
        try:
            repo_rel = candidate.relative_to(repo_root_resolved).as_posix()
        except ValueError:
            continue
        if not candidate.is_file() or not is_source_ingest_criterion_path(repo_rel):
            continue
        if repo_rel not in seen:
            seen.add(repo_rel)
            found.append(repo_rel)
    return found


def source_criterion_applies_to_note(repo_root: Path, note_abs: Path, criterion_path: str) -> bool:
    """Whether the current artifact resolves a link to this ingest criterion."""
    if not is_source_ingest_criterion_path(criterion_path):
        return False
    return criterion_path in note_source_ingest_paths(repo_root, note_abs)
