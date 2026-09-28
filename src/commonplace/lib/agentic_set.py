"""Analysis-specific views over the shared directory artifact loader."""

from __future__ import annotations

import re
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path, PurePosixPath
from typing import TYPE_CHECKING, Any

from commonplace.lib.directory_artifact import MANIFEST_NAME, DirectoryArtifact

if TYPE_CHECKING:
    from commonplace.lib.validation import ValidationRun

from commonplace.lib.note_parser import ParsedDocument

REVIEW_TYPE = "agentic-systems/types/generated-review.md"

SET_TYPE = "reports/types/agentic-system-analysis-set.md"
OUTPUT_DIR = "output"

OVERVIEW_NAME = "overview.md"
MEMBER_NAMES = ("runtime.md", "memory.md", "epistemic.md")
SET_NAMES = (OVERVIEW_NAME, *MEMBER_NAMES)
LOCAL_REPORT_NAME = "memory-report.md"
LOCAL_INPUT_NAME = "memory-input.md"

RETAINED_ROOT = Path("kb/reports/retained/agentic-system-analysis")
REVIEWS_ROOT = PurePosixPath("kb/agentic-systems/reviews")
RUN_ID = re.compile(r"AAS-\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*-\d{2}")


def is_normalized_relative(value: str) -> bool:
    """Whether ``value`` is a nonempty relative POSIX path with no ``..`` or redundancy."""
    pure = PurePosixPath(value)
    return bool(pure.parts) and not pure.is_absolute() and value == pure.as_posix() and (
        ".." not in pure.parts
    )


def is_review_path(value: str) -> bool:
    """Whether ``value`` names a generated review: ``kb/agentic-systems/reviews/<name>.md``."""
    pure = PurePosixPath(value)
    return is_normalized_relative(value) and pure.parent == REVIEWS_ROOT and pure.suffix == ".md"



def retained_overview_path(run_id: str) -> Path:
    if not isinstance(run_id, str) or not RUN_ID.fullmatch(run_id):
        raise ValueError("invalid analysis run ID")
    return RETAINED_ROOT / run_id / OVERVIEW_NAME


def retained_artifact_path(run_id: str) -> Path:
    return retained_overview_path(run_id).with_name(MANIFEST_NAME)


def retained_set_paths(run_id: str) -> dict[str, Path]:
    """Repository-relative retained path of every set document, by name."""
    directory = retained_overview_path(run_id).parent
    return {name: directory / name for name in (MANIFEST_NAME, *SET_NAMES)}


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
    artifact: DirectoryArtifact
    overview: SetDocument
    members: dict[str, SetDocument]

    @property
    def documents(self) -> list[SetDocument]:
        return [self.overview, *self.members.values()]

    @property
    def memory(self) -> SetDocument | None:
        return self.members.get("memory.md")


def from_artifact(artifact: DirectoryArtifact) -> MemberSet:
    documents = {
        name: SetDocument(name, member.path, member.content, member.document)
        for name, member in artifact.members.items()
    }
    overview = documents.pop(OVERVIEW_NAME)
    return MemberSet(artifact, overview, documents)


def load_member_set(directory: Path, *, run: ValidationRun) -> MemberSet:
    """Validate one analysis artifact through the caller's shared context."""
    checked = run.validate(directory)
    if checked.fails or checked.warns:
        raise ValueError("; ".join([*checked.fails, *checked.warns]))
    artifact = run.artifact(directory)
    if artifact.manifest.get("type") != SET_TYPE:
        raise ValueError(f"expected analysis artifact type {SET_TYPE}")
    return from_artifact(artifact)


def set_identity_errors(
    member_set: MemberSet,
) -> list[str]:
    """Check that every member carries the overview's run and boundary identity."""
    overview = member_set.overview.frontmatter
    run_id = overview.get("run-id")
    boundary = overview.get("reviewed-boundary")
    errors: list[str] = []
    for name, member in member_set.members.items():
        values = member.frontmatter
        if values.get("run-id") != run_id:
            errors.append(f"{name}: run-id does not match the overview")
        if values.get("reviewed-boundary") != boundary:
            errors.append(f"{name}: reviewed-boundary does not match the overview")
    return errors

