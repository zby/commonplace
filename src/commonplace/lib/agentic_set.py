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
from pathlib import Path
from typing import Any

from commonplace.lib.agentic_records import PROPOSAL_TOKEN, RECORD_ID, section
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
RUN_ID = re.compile(r"AAS-\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*-\d{2}")
_SHA256 = re.compile(r"^[0-9a-f]{64}$")

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
    complete = overview.frontmatter.get("result-disposition") == "complete"
    names = [entry.get("path") if isinstance(entry, Mapping) else None for entry in manifest]
    if complete:
        if sorted(name for name in names if isinstance(name, str)) != sorted(MEMBER_TYPES):
            raise ValueError(
                "manifest: a complete overview names exactly "
                + ", ".join(MEMBER_TYPES)
            )
    elif manifest:
        raise ValueError("manifest: a blocked or out-of-scope overview names no members")

    members: dict[str, SetDocument] = {}
    for entry in manifest:
        if not isinstance(entry, Mapping) or set(entry) != {"path", "sha256", "type"}:
            raise ValueError("manifest: each member entry has path, sha256 and type")
        name = entry["path"]
        expected_type = MEMBER_TYPES.get(name)
        if expected_type is None:
            raise ValueError(f"manifest: unknown member name {name!r}")
        if entry["type"] != expected_type:
            raise ValueError(f"manifest: {name} must have type {expected_type}")
        if not isinstance(entry["sha256"], str) or not _SHA256.fullmatch(entry["sha256"]):
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
        run_field = "analysis-run" if name == "memory.md" else "run-id"
        if values.get(run_field) != run_id:
            errors.append(f"{name}: {run_field} does not match the overview")
        if values.get("reviewed-boundary") != boundary:
            errors.append(f"{name}: reviewed-boundary does not match the overview")
        if name == "memory.md" and source_identity is not None and (
            values.get("source-identity") != source_identity
        ):
            errors.append(f"{name}: source-identity does not match the frozen source")
    return errors


def declared_union(member_set: MemberSet) -> set[str]:
    """Every canonical ID declared across the members plus the register's sources."""
    from commonplace.lib.agentic_records import declared_ids, source_ids

    declared = source_ids(member_set.overview.body)
    for member in member_set.members.values():
        declared.update(declared_ids(member.body))
    return declared


# --- finalization of the memory member ---------------------------------------

_TABLE_ROW = re.compile(r"^\s*\|(.*)\|\s*$")
_HEADING_DECLARATION = re.compile(
    rf"(?m)^([ \t]*#{{3,6}}[ \t]+)({RECORD_ID})(?![\w-])"
)


def _cell_token(cell: str) -> str:
    return cell.strip().strip("`*").strip()


def proposal_mapping(overview_body: str) -> dict[str, str]:
    """The Reconciliation mapping table: specialist proposal to canonical record.

    A row maps when its first cell is one proposal ID and its second cell is
    one canonical ID; other rows are prose. A proposal mapped twice is an
    error, since exact-token replacement needs one target per token.
    """
    mapping: dict[str, str] = {}
    for line in section(overview_body, "Reconciliation").splitlines():
        row = _TABLE_ROW.match(line)
        if row is None:
            continue
        cells = [_cell_token(cell) for cell in row.group(1).split("|")]
        if len(cells) < 2:
            continue
        proposal, canonical = cells[0], cells[1]
        if not PROPOSAL_TOKEN.fullmatch(proposal) or not re.fullmatch(RECORD_ID, canonical):
            continue
        if proposal in mapping and mapping[proposal] != canonical:
            raise ValueError(f"reconciliation mapping: {proposal} mapped twice")
        mapping[proposal] = canonical
    return mapping


def finalize_local_report(text: str, mapping: Mapping[str, str]) -> str:
    """Derive the finalized memory member's text from the local report.

    Proposal IDs are replaced by exact-token mapping across the whole text,
    frontmatter included. Under ``## Shared records`` a heading that declares
    a canonical ID which no proposal mapped to is a seeded record the
    specialist re-declared, so it becomes an ``On <ID>`` annotation heading.
    The ``## Amendments`` section and ``finalized-from`` are authored on top
    and are not derived here.
    """
    mapped = PROPOSAL_TOKEN.sub(lambda m: mapping.get(m.group(0), m.group(0)), text)
    registered = set(mapping.values())
    match = re.search(r"(?ms)^## Shared records[ \t]*\n.*?(?=^## |\Z)", mapped)
    if match is None:
        return mapped
    shared = match.group(0)
    rewritten = _HEADING_DECLARATION.sub(
        lambda m: m.group(0) if m.group(2) in registered else f"{m.group(1)}On {m.group(2)}",
        shared,
    )
    return mapped[: match.start()] + rewritten + mapped[match.end() :]


def _normalize(text: str) -> str:
    return " ".join(text.split())


def strip_amendments(body: str) -> str:
    return re.sub(r"(?ms)^## Amendments[ \t]*\n.*?(?=^## |\Z)", "", body)


def finalization_errors(
    *, local_text: str, member: SetDocument, mapping: Mapping[str, str]
) -> list[str]:
    """Check that the memory member is the local report finalized and nothing more."""
    derived, error = parse_document(finalize_local_report(local_text, mapping))
    if error is not None or derived is None or derived.frontmatter is None:
        return ["finalization: the mapped local report is not parseable"]
    errors: list[str] = []
    expected = dict(derived.frontmatter)
    actual = dict(member.frontmatter)
    expected.pop("finalized-from", None)
    actual.pop("finalized-from", None)
    if expected != actual:
        errors.append(
            "finalization: memory member frontmatter differs from the mapped local "
            "report beyond finalized-from"
        )
    if "## Amendments" not in member.body.split("\n"):
        errors.append("finalization: memory member lacks its ## Amendments section")
    if _normalize(strip_amendments(member.body)) != _normalize(derived.body):
        errors.append(
            "finalization: memory member body differs from the mapped local report "
            "outside ## Amendments"
        )
    return errors
