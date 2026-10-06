"""Analysis-specific views over the shared directory artifact loader."""

from __future__ import annotations

import re
from dataclasses import dataclass
from functools import cache
from hashlib import sha256
from pathlib import Path, PurePosixPath
from typing import TYPE_CHECKING, Any
from urllib.parse import urlsplit, urlunsplit

from commonplace.lib.directory_artifact import DirectoryArtifact
from commonplace.lib.directory_layout import Layout, parse_layout

if TYPE_CHECKING:
    from commonplace.lib.validation import ValidationRun

from commonplace.lib.note_parser import ParsedDocument

SET_TYPE = "agentic-system-analyses/types/agentic-system-analysis-set.md"
OUTPUT_DIR = "output"

RETAINED_ROOT = Path("kb/agentic-system-analyses/retained")
REVIEWS_ROOT = PurePosixPath(RETAINED_ROOT.as_posix())
ARCHIVE_ROOT = Path("kb/agentic-system-analyses/retained-archive")
RUN_ID = re.compile(r"AAS-\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*-\d{2}")


def analysis_layout() -> Layout:
    """The set type's declared layout, from the library this process runs."""
    from commonplace.lib.library import library_root

    return _layout_at(str(library_root()))


@cache
def _layout_at(library: str) -> Layout:
    from commonplace.lib import frontmatter

    parsed = frontmatter.parse((Path(library) / SET_TYPE).read_text(encoding="utf-8"))
    if parsed.errors:
        raise ValueError(f"{SET_TYPE}: {'; '.join(parsed.errors)}")
    return parse_layout(parsed.data.get("layout"), where=f"{SET_TYPE}: layout")


def is_normalized_relative(value: str) -> bool:
    """Whether ``value`` is a nonempty relative POSIX path with no ``..`` or redundancy."""
    pure = PurePosixPath(value)
    return bool(pure.parts) and not pure.is_absolute() and value == pure.as_posix() and (
        ".." not in pure.parts
    )


def is_review_path(value: str) -> bool:
    """Whether ``value`` names a current accepted overview at its stable path."""
    pure = PurePosixPath(value)
    return (is_normalized_relative(value) and pure.name == analysis_layout().path("overview")
            and pure.parent.parent == REVIEWS_ROOT)


def normalize_source_identity(identity: str) -> str:
    """One form of a source identity: surrounding whitespace, a trailing ``/``
    and a trailing ``.git`` removed, and a URL's scheme and host lowercased.

    It decides only between forms of one identity, not whether two different
    URLs name one repository.
    """
    value = identity.strip().rstrip("/").removesuffix(".git")
    parts = urlsplit(value)
    if not (parts.scheme and parts.netloc):
        return value
    user, at, host = parts.netloc.rpartition("@")
    return urlunsplit(parts._replace(netloc=f"{user}{at}{host.lower()}"))


@dataclass(frozen=True)
class SetDocument:
    name: str
    path: Path
    content: bytes
    document: ParsedDocument

    @property
    def text(self) -> str:
        return self.content.decode("utf-8")

    @property
    def frontmatter(self) -> dict[str, Any]:
        return self.document.frontmatter or {}

    @property
    def body(self) -> str:
        return self.document.body

    @property
    def sha256(self) -> str:
        return sha256(self.content).hexdigest()


@dataclass(frozen=True)
class MemberSet:
    """One analysis set's documents, by layout role."""

    artifact: DirectoryArtifact
    roles: dict[str, SetDocument]

    @property
    def documents(self) -> list[SetDocument]:
        return list(self.roles.values())

    @property
    def overview(self) -> SetDocument:
        return self.roles["overview"]

    @property
    def memory(self) -> SetDocument | None:
        return self.roles.get("memory")

    @property
    def profile(self) -> SetDocument | None:
        return self.roles.get("memory-profile")


def from_artifact(artifact: DirectoryArtifact, layout: Layout | None = None) -> MemberSet:
    """The members that have a layout role; a missing overview is an error."""
    layout = layout or analysis_layout()
    roles = {}
    for role in layout.roles.values():
        member = artifact.members.get(role.path)
        if member is not None:
            roles[role.name] = SetDocument(role.path, member.path, member.content, member.document)
    if "overview" not in roles:
        raise ValueError(f"analysis set has no {layout.path('overview')}")
    return MemberSet(artifact, roles)


def load_member_set(directory: Path, *, run: ValidationRun) -> MemberSet:
    """Validate one analysis artifact through the caller's shared context."""
    checked = run.validate(directory)
    if checked.fails or checked.warns:
        raise ValueError("; ".join([*checked.fails, *checked.warns]))
    artifact = run.artifact(directory)
    if artifact.manifest.get("type") != SET_TYPE:
        raise ValueError(f"expected analysis artifact type {SET_TYPE}")
    return from_artifact(artifact)


def source_slug(identity: str, system: str) -> str:
    """Use the workflow's source segment, or its system fallback, as the slug."""
    parts = urlsplit(normalize_source_identity(identity))
    segment = parts.path.rsplit("/", 1)[-1]
    name = segment if parts.scheme and parts.netloc and segment else system
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    if not slug:
        raise ValueError("neither the source identity nor the system names the run")
    return slug


def current_analyses(repo_root: Path, *, run=None) -> list[MemberSet]:
    """Enumerate and validate one current set per source at its stable path."""
    from commonplace.lib.validation import ValidationRun

    root = repo_root.resolve()
    run = run or ValidationRun(root, ())
    result = []
    identities = set()
    directories = sorted((root / RETAINED_ROOT).iterdir()) if (root / RETAINED_ROOT).exists() else ()
    # Diagnose duplicates before a misplaced copy's path-name error hides them.
    from commonplace.lib.note_parser import parse_document
    memory = analysis_layout().path("memory")
    for directory in directories:
        if directory.name.startswith(".") or not (directory / memory).is_file():
            continue
        document, error = parse_document(run.read_bytes(directory / memory).decode("utf-8"))
        identity = (document.frontmatter or {}).get("source-identity") if document is not None and error is None else None
        if isinstance(identity, str):
            identity = normalize_source_identity(identity)
            if identity in identities:
                raise ValueError(f"multiple current analyses of source {identity}")
            identities.add(identity)
    identities.clear()
    for directory in directories:
        if directory.name.startswith("."):
            continue
        if not directory.is_dir() or directory.is_symlink():
            raise ValueError(f"current analysis must be a directory: {directory}")
        member_set = load_member_set(directory, run=run)
        data = member_set.overview.frontmatter
        if data.get("result-disposition") != "complete" or member_set.memory is None:
            raise ValueError(f"current analysis must be complete: {directory}")
        identity = normalize_source_identity(member_set.memory.frontmatter.get("source-identity", ""))
        if not identity:
            raise ValueError(f"current analysis lacks source identity: {directory}")
        if identity in identities:
            raise ValueError(f"multiple current analyses of source {identity}")
        identities.add(identity)
        if directory.name != source_slug(identity, data["system"]):
            raise ValueError(f"current directory name does not match its source: {directory}")
        result.append(member_set)
    return result
