"""Load and check the member set of one agentic-system analysis run.

A run's retained output is a set: the overview, whose frontmatter manifest
pins the other members by path, SHA-256 and type, plus the runtime, memory
and epistemic members. Every reader verifies the manifest before opening a
member; these helpers are that verification, shared by run-state
verification, publication and the comparison loader.
"""

from __future__ import annotations

import re
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path, PurePosixPath
from typing import Any

from commonplace.lib.note_parser import ParsedDocument, parse_document

OVERVIEW_TYPE = "types/agentic-system-analysis-overview.md"
RUNTIME_TYPE = "types/agentic-system-runtime-report.md"
MEMORY_TYPE = "types/agent-memory-analysis-report.md"
EPISTEMIC_TYPE = "types/agentic-system-epistemic-report.md"
REVIEW_TYPE = "agentic-systems/types/generated-review.md"

OVERVIEW_NAME = "overview.md"
MEMBER_TYPES: dict[str, str] = {
    "runtime.md": RUNTIME_TYPE,
    "memory.md": MEMORY_TYPE,
    "epistemic.md": EPISTEMIC_TYPE,
}
SET_NAMES = (OVERVIEW_NAME, *MEMBER_TYPES)
LOCAL_REPORT_NAME = "memory-report.md"
LOCAL_INPUT_NAME = "memory-input.md"

RETAINED_ROOT = Path("kb/reports/retained/agentic-system-analysis")
REVIEWS_ROOT = PurePosixPath("kb/agentic-systems/reviews")
RUN_ID = re.compile(r"AAS-\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*-\d{2}")
SHA256 = re.compile(r"[0-9a-f]{64}")
"""A lowercase SHA-256 hex digest; use with ``fullmatch``."""


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

Reader = Callable[[Path], bytes]


def retained_overview_path(run_id: str) -> Path:
    if not isinstance(run_id, str) or not RUN_ID.fullmatch(run_id):
        raise ValueError("invalid analysis run ID")
    return RETAINED_ROOT / run_id / OVERVIEW_NAME


def retained_set_paths(run_id: str) -> dict[str, Path]:
    """Repository-relative retained path of every set document, by name."""
    directory = retained_overview_path(run_id).parent
    return {name: directory / name for name in SET_NAMES}


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
    overview: SetDocument
    members: dict[str, SetDocument]

    @property
    def documents(self) -> list[SetDocument]:
        return [self.overview, *self.members.values()]

    @property
    def memory(self) -> SetDocument | None:
        return self.members.get("memory.md")


def parse_set_document(name: str, path: Path, content: bytes) -> SetDocument:
    try:
        text = content.decode("utf-8")
    except UnicodeError as exc:
        raise ValueError(f"{name}: not UTF-8 text") from exc
    document, error = parse_document(text)
    if error is not None or document is None or document.frontmatter is None:
        raise ValueError(f"{name}: frontmatter is not parseable")
    return SetDocument(name=name, path=path, content=content, document=document)


def _read(path: Path, read: Reader | None) -> bytes:
    try:
        return read(path) if read is not None else path.read_bytes()
    except OSError as exc:
        raise ValueError(f"cannot read {path.name}: {exc}") from exc


def load_member_set(overview_path: Path, *, read: Reader | None = None) -> MemberSet:
    """Open the overview, verify its manifest, and open every member it pins.

    ``read`` replaces the file read so callers can supply candidate bytes.
    A failed check raises ``ValueError`` naming the check.
    """
    overview = parse_set_document(OVERVIEW_NAME, overview_path, _read(overview_path, read))
    if overview.frontmatter.get("type") != OVERVIEW_TYPE:
        raise ValueError(f"{OVERVIEW_NAME}: expected type {OVERVIEW_TYPE}")
    manifest = overview.frontmatter.get("members")
    if not isinstance(manifest, list):
        raise ValueError("manifest: members must be a list")  # noqa: TRY004
    for index, entry in enumerate(manifest, start=1):
        if not isinstance(entry, Mapping) or set(entry) != {"path", "sha256", "type"}:
            raise ValueError(
                f"manifest: entry {index} must have exactly path, sha256 and type"
            )
        for field in ("path", "sha256", "type"):
            if not isinstance(entry[field], str):
                raise ValueError(  # noqa: TRY004
                    f"manifest: entry {index} ({entry['path']!r}) needs a string {field}"
                )
    complete = overview.frontmatter.get("result-disposition") == "complete"
    if complete:
        if sorted(entry["path"] for entry in manifest) != sorted(MEMBER_TYPES):
            raise ValueError(
                "manifest: a complete overview names exactly "
                + ", ".join(MEMBER_TYPES)
            )
    elif manifest:
        raise ValueError("manifest: a blocked or out-of-scope overview names no members")

    members: dict[str, SetDocument] = {}
    for entry in manifest:
        name = entry["path"]
        expected_type = MEMBER_TYPES.get(name)
        if expected_type is None:
            raise ValueError(f"manifest: unknown member name {name!r}")
        if entry["type"] != expected_type:
            raise ValueError(f"manifest: {name} must have type {expected_type}")
        if not SHA256.fullmatch(entry["sha256"]):
            raise ValueError(f"manifest: {name} needs a lowercase SHA-256 digest")
        path = overview_path.parent / name
        content = _read(path, read)
        actual = sha256(content).hexdigest()
        if actual != entry["sha256"]:
            raise ValueError(
                f"manifest: {name} bytes hash to {actual}, expected {entry['sha256']}"
            )
        member = parse_set_document(name, path, content)
        if member.frontmatter.get("type") != expected_type:
            raise ValueError(f"{name}: expected type {expected_type}")
        members[name] = member
    return MemberSet(overview=overview, members=members)


def set_identity_errors(
    member_set: MemberSet,
    *,
    source_identity: str | None = None,
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
        if name == "memory.md" and source_identity is not None and (
            values.get("source-identity") != source_identity
        ):
            errors.append(f"{name}: source-identity does not match the frozen source")
    return errors

