"""Analysis-specific views over the shared directory artifact loader."""

from __future__ import annotations

import re
from dataclasses import dataclass
from functools import cache
from hashlib import sha256
from pathlib import Path, PurePosixPath
from typing import TYPE_CHECKING, Any
from urllib.parse import urlsplit

import yaml

from commonplace.lib.directory_artifact import DirectoryArtifact
from commonplace.lib.directory_layout import Layout, parse_layout

if TYPE_CHECKING:
    from commonplace.lib.validation import ValidationRun

from commonplace.lib.note_parser import ParsedDocument
from commonplace.lib.quote_grounding import is_normalized_relative
from commonplace.lib.source_identity import normalize_source_identity

ANALYSIS_TYPE = "agentic-system-analyses/types/agentic-system-analysis-set.md"

RETAINED_ROOT = Path("kb/agentic-system-analyses/retained")
ARCHIVE_ROOT = Path("kb/agentic-system-analyses/retained-archive")
CAPTURE_DIRECTORY = "sources"
"""Where, under the run directory, a boundary freezes non-Git captures; the plan prints it."""


def analysis_layout() -> Layout:
    """The artifact type's declared layout, from the library this process runs."""
    from commonplace.lib.library import library_root

    return _layout_at(str(library_root()))


@cache
def _spec_at(library: str, type_path: str) -> dict[str, Any]:
    from commonplace.lib import frontmatter

    parsed = frontmatter.parse((Path(library) / type_path).read_text(encoding="utf-8"))
    if parsed.errors:
        raise ValueError(f"{type_path}: {'; '.join(parsed.errors)}")
    return parsed.data


@cache
def _layout_at(library: str) -> Layout:
    return parse_layout(_spec_at(library, ANALYSIS_TYPE).get("layout"), where=f"{ANALYSIS_TYPE}: layout")


def is_review_path(value: str) -> bool:
    """Whether ``value`` names a current accepted overview at its stable path."""
    pure = PurePosixPath(value)
    return (is_normalized_relative(value) and pure.name == analysis_layout().path("overview")
            and pure.parent.parent == PurePosixPath(RETAINED_ROOT.as_posix()))


@dataclass(frozen=True)
class Member:
    name: str
    path: Path
    content: bytes
    document: ParsedDocument

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
class Analysis:
    """One analysis artifact's documents, by layout role."""

    artifact: DirectoryArtifact
    roles: dict[str, Member]

    @property
    def documents(self) -> list[Member]:
        return list(self.roles.values())

    @property
    def overview(self) -> Member:
        return self.roles["overview"]

    @property
    def memory(self) -> Member | None:
        return self.roles.get("memory")

    @property
    def memory_profile(self) -> Member | None:
        return self.roles.get("memory-profile")


def from_artifact(artifact: DirectoryArtifact, layout: Layout | None = None) -> Analysis:
    """The members that have a layout role; a missing overview is an error."""
    layout = layout or analysis_layout()
    roles = {}
    for role in layout.roles.values():
        member = artifact.members.get(role.path)
        if member is not None:
            roles[role.name] = Member(role.path, member.path, member.content, member.document)
    if "overview" not in roles:
        raise ValueError(f"analysis artifact has no {layout.path('overview')}")
    return Analysis(artifact, roles)


def load_analysis(directory: Path, *, run: ValidationRun) -> Analysis:
    """Validate one analysis artifact through the caller's shared context."""
    checked = run.validate(directory)
    if checked.fails or checked.warns:
        raise ValueError("; ".join([*checked.fails, *checked.warns]))
    artifact = run.artifact(directory)
    if artifact.manifest.get("type") != ANALYSIS_TYPE:
        raise ValueError(f"expected analysis artifact type {ANALYSIS_TYPE}")
    return from_artifact(artifact)


WORKER_PROFILES = "agentic-system-analyses/instructions/analyse-agentic-system/worker-profiles.yaml"
"""Library-relative path of the named worker identities a run chooses from."""


def resolve_worker_profile(data: bytes, name: str | None, *, harness: str | None = None) -> dict[str, str]:
    """Resolve a worker profile by name, or the harness's default, to its identity.

    A named profile must belong to ``harness`` when one is given.
    """
    parsed = yaml.safe_load(data)
    profiles = parsed.get("profiles") if isinstance(parsed, dict) else None
    defaults = parsed.get("defaults") if isinstance(parsed, dict) else None
    if not isinstance(profiles, dict) or not profiles or not isinstance(defaults, dict):
        raise ValueError("worker profiles need nonempty profiles and a defaults mapping")
    if name is None:
        if harness not in defaults:
            raise ValueError(f"name a worker profile or a harness with a default: {', '.join(sorted(defaults))}")
        name = defaults[harness]
    if name not in profiles:
        raise ValueError(f"unknown worker profile {name!r}; choose one of {', '.join(sorted(profiles))}")
    profile = profiles[name]
    fields = ("harness", "launch-model", "effort")
    if (not isinstance(profile, dict) or set(profile) != set(fields)
            or any(not isinstance(profile[field], str) or not profile[field].strip() for field in fields)):
        raise ValueError(f"worker profile {name} needs exactly a harness, launch-model and effort")
    if harness is not None and profile["harness"] != harness:
        raise ValueError(f"worker profile {name} runs in {profile['harness']}, not {harness}")
    return {"profile": name, **{field: profile[field] for field in fields}}


def source_slug(identity: str, system: str) -> str:
    """Use the workflow's source segment, or its system fallback, as the slug."""
    parts = urlsplit(normalize_source_identity(identity))
    segment = parts.path.rsplit("/", 1)[-1]
    name = segment if parts.scheme and parts.netloc and segment else system
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    if not slug:
        raise ValueError("neither the source identity nor the system names the run")
    return slug


def current_analyses(repo_root: Path, *, run=None) -> list[Analysis]:
    """Enumerate and validate one current artifact per source at its stable path."""
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
        analysis = load_analysis(directory, run=run)
        data = analysis.overview.frontmatter
        if data.get("result-disposition") != "complete" or analysis.memory is None:
            raise ValueError(f"current analysis must be complete: {directory}")
        identity = normalize_source_identity(analysis.memory.frontmatter.get("source-identity", ""))
        if not identity:
            raise ValueError(f"current analysis lacks source identity: {directory}")
        if identity in identities:
            raise ValueError(f"multiple current analyses of source {identity}")
        identities.add(identity)
        if directory.name != source_slug(identity, data["system"]):
            raise ValueError(f"current directory name does not match its source: {directory}")
        result.append(analysis)
    return result
