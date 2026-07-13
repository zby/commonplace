"""Full-pass report parsing, capture verification, and transition guarding."""

from __future__ import annotations

import difflib
import re
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Literal

from commonplace.lib.hashing import content_sha256_for_text
from commonplace.lib.note_parser import ParsedDocument, parse_document


FULL_PASS_REPORT_TYPE = "kb/reports/types/full-pass-report.md"
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
_RESOLUTION_HEADING_RE = re.compile(r"^## Resolution\s*$", re.MULTILINE)
_NEXT_H2_RE = re.compile(r"^## (?!Resolution\s*$).+$", re.MULTILINE)

GuardStatus = Literal["matching", "changed", "missing", "corrupt-capture"]


@dataclass(frozen=True)
class GuardedInput:
    role: Literal["source", "merge-target"]
    logical_path: str
    logical_file: Path
    capture_path: str
    capture_file: Path
    expected_sha256: str


@dataclass(frozen=True)
class FullPassReport:
    path: Path
    packet_dir: Path
    frontmatter: dict[str, Any]
    body: str
    disposition: Literal["keep", "delete", "merge"]
    guarded_inputs: tuple[GuardedInput, ...]


@dataclass(frozen=True)
class GuardResult:
    role: str
    logical_path: str
    capture_path: str
    expected_sha256: str
    status: GuardStatus
    capture_sha256: str | None = None
    current_sha256: str | None = None
    diff: str | None = None
    detail: str | None = None

    def to_dict(self) -> dict[str, str | None]:
        return {
            "role": self.role,
            "logical_path": self.logical_path,
            "capture_path": self.capture_path,
            "expected_sha256": self.expected_sha256,
            "status": self.status,
            "capture_sha256": self.capture_sha256,
            "current_sha256": self.current_sha256,
            "diff": self.diff,
            "detail": self.detail,
        }


def _required_string(frontmatter: dict[str, Any], field: str) -> str:
    value = frontmatter.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field}: expected a non-empty string")
    return value


def _required_sha256(frontmatter: dict[str, Any], field: str) -> str:
    value = _required_string(frontmatter, field)
    if not _SHA256_RE.fullmatch(value):
        raise ValueError(f"{field}: expected a lowercase SHA-256 hex digest")
    return value


def _repo_relative_file(value: str, *, repo_root: Path, field: str) -> Path:
    pure = PurePosixPath(value)
    if pure.is_absolute() or value != pure.as_posix() or ".." in pure.parts:
        raise ValueError(f"{field}: expected a normalized repository-relative path")
    if not pure.parts or pure.parts[0] != "kb":
        raise ValueError(f"{field}: expected a repository-relative path under kb/")
    candidate = repo_root.joinpath(*pure.parts)
    try:
        candidate.resolve(strict=False).relative_to(repo_root)
    except ValueError as exc:
        raise ValueError(f"{field}: path escapes the repository") from exc
    return candidate


def _capture_file(value: str, *, packet_dir: Path, field: str) -> Path:
    pure = PurePosixPath(value)
    if (
        pure.is_absolute()
        or value != pure.as_posix()
        or ".." in pure.parts
        or not pure.parts
        or pure.suffix != ".txt"
    ):
        raise ValueError(f"{field}: expected a normalized packet-relative .txt path")
    candidate = packet_dir.joinpath(*pure.parts)
    try:
        candidate.resolve(strict=False).relative_to(packet_dir.resolve())
    except ValueError as exc:
        raise ValueError(f"{field}: capture path escapes its packet") from exc
    return candidate


def _guarded_input(
    frontmatter: dict[str, Any],
    *,
    role: Literal["source", "merge-target"],
    logical_field: str,
    capture_field: str,
    hash_field: str,
    packet_dir: Path,
    repo_root: Path,
) -> GuardedInput:
    logical_path = _required_string(frontmatter, logical_field)
    capture_path = _required_string(frontmatter, capture_field)
    return GuardedInput(
        role=role,
        logical_path=logical_path,
        logical_file=_repo_relative_file(
            logical_path, repo_root=repo_root, field=logical_field
        ),
        capture_path=capture_path,
        capture_file=_capture_file(
            capture_path, packet_dir=packet_dir, field=capture_field
        ),
        expected_sha256=_required_sha256(frontmatter, hash_field),
    )


def parse_full_pass_report(
    path: Path,
    document: ParsedDocument,
    *,
    repo_root: Path,
) -> FullPassReport:
    """Build the full-pass runtime view from an already parsed report."""
    repo_root = repo_root.resolve()
    report_path = path.resolve()
    reports_root = (repo_root / "kb" / "reports" / "full-pass").resolve()
    try:
        report_path.relative_to(reports_root)
    except ValueError as exc:
        raise ValueError(
            "report path: expected a file under kb/reports/full-pass/"
        ) from exc

    frontmatter = document.frontmatter
    if frontmatter is None:
        raise ValueError("report: missing frontmatter")
    if frontmatter.get("type") != FULL_PASS_REPORT_TYPE:
        raise ValueError(f"type: expected {FULL_PASS_REPORT_TYPE}")

    disposition_value = frontmatter.get("disposition")
    if disposition_value not in {"keep", "delete", "merge"}:
        raise ValueError("disposition: expected keep, delete, or merge")
    disposition: Literal["keep", "delete", "merge"] = disposition_value

    packet_dir = report_path.parent
    guarded_inputs = [
        _guarded_input(
            frontmatter,
            role="source",
            logical_field="source",
            capture_field="source_capture",
            hash_field="source_sha256",
            packet_dir=packet_dir,
            repo_root=repo_root,
        )
    ]

    merge_fields = (
        "merge_target",
        "merge_target_capture",
        "merge_target_title",
        "merge_target_sha256",
    )
    if disposition == "merge":
        _required_string(frontmatter, "merge_target_title")
        guarded_inputs.append(
            _guarded_input(
                frontmatter,
                role="merge-target",
                logical_field="merge_target",
                capture_field="merge_target_capture",
                hash_field="merge_target_sha256",
                packet_dir=packet_dir,
                repo_root=repo_root,
            )
        )
    elif any(frontmatter.get(field) is not None for field in merge_fields):
        raise ValueError("merge fields: expected null unless disposition is merge")

    return FullPassReport(
        path=report_path,
        packet_dir=packet_dir,
        frontmatter=frontmatter,
        body=document.body,
        disposition=disposition,
        guarded_inputs=tuple(guarded_inputs),
    )


def load_full_pass_report(path: Path, *, repo_root: Path) -> FullPassReport:
    """Read and parse one full-pass report for guarding or inspection."""
    repo_root = repo_root.resolve()
    candidate = path if path.is_absolute() else repo_root / path
    if candidate.is_symlink() or not candidate.is_file():
        raise FileNotFoundError(f"report path: not a regular non-symlink file: {path}")
    content = candidate.read_text(encoding="utf-8")
    document, error = parse_document(content)
    if error or document is None:
        raise ValueError(f"report: {error or 'could not parse'}")
    return parse_full_pass_report(candidate, document, repo_root=repo_root)


def _symlink_in_packet_path(guarded_input: GuardedInput, packet_dir: Path) -> bool:
    cursor = packet_dir
    relative = PurePosixPath(guarded_input.capture_path)
    for part in relative.parts:
        cursor = cursor / part
        if cursor.is_symlink():
            return True
    return False


def verify_capture(
    guarded_input: GuardedInput, *, packet_dir: Path
) -> tuple[str | None, str | None, str | None]:
    """Return capture text, actual hash, and an error detail."""
    capture = guarded_input.capture_file
    if _symlink_in_packet_path(guarded_input, packet_dir):
        return None, None, "capture path contains a symlink"
    if not capture.is_file():
        return None, None, "capture is missing or is not a regular file"
    try:
        text = capture.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return None, None, f"capture cannot be read as UTF-8 text: {exc}"
    actual_sha256 = content_sha256_for_text(text)
    if actual_sha256 != guarded_input.expected_sha256:
        return text, actual_sha256, "capture content does not match its recorded hash"
    return text, actual_sha256, None


def guard_input(guarded_input: GuardedInput, *, packet_dir: Path) -> GuardResult:
    capture_text, capture_sha256, capture_error = verify_capture(
        guarded_input, packet_dir=packet_dir
    )
    if capture_error is not None:
        return GuardResult(
            role=guarded_input.role,
            logical_path=guarded_input.logical_path,
            capture_path=guarded_input.capture_path,
            expected_sha256=guarded_input.expected_sha256,
            capture_sha256=capture_sha256,
            status="corrupt-capture",
            detail=capture_error,
        )

    current = guarded_input.logical_file
    if current.is_symlink() or not current.is_file():
        return GuardResult(
            role=guarded_input.role,
            logical_path=guarded_input.logical_path,
            capture_path=guarded_input.capture_path,
            expected_sha256=guarded_input.expected_sha256,
            capture_sha256=capture_sha256,
            status="missing",
            detail="live artifact is missing or is not a regular non-symlink file",
        )
    try:
        current_text = current.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return GuardResult(
            role=guarded_input.role,
            logical_path=guarded_input.logical_path,
            capture_path=guarded_input.capture_path,
            expected_sha256=guarded_input.expected_sha256,
            capture_sha256=capture_sha256,
            status="missing",
            detail=f"live artifact cannot be read as UTF-8 text: {exc}",
        )

    current_sha256 = content_sha256_for_text(current_text)
    if current_sha256 == guarded_input.expected_sha256:
        return GuardResult(
            role=guarded_input.role,
            logical_path=guarded_input.logical_path,
            capture_path=guarded_input.capture_path,
            expected_sha256=guarded_input.expected_sha256,
            capture_sha256=capture_sha256,
            current_sha256=current_sha256,
            status="matching",
        )

    assert capture_text is not None
    diff = "".join(
        difflib.unified_diff(
            capture_text.splitlines(keepends=True),
            current_text.splitlines(keepends=True),
            fromfile=guarded_input.capture_path,
            tofile=guarded_input.logical_path,
        )
    )
    return GuardResult(
        role=guarded_input.role,
        logical_path=guarded_input.logical_path,
        capture_path=guarded_input.capture_path,
        expected_sha256=guarded_input.expected_sha256,
        capture_sha256=capture_sha256,
        current_sha256=current_sha256,
        status="changed",
        diff=diff,
        detail="live artifact differs from the packet capture",
    )


def guard_full_pass_report(report: FullPassReport) -> tuple[GuardResult, ...]:
    """Compare every report-owned capture with its current logical artifact."""
    return tuple(
        guard_input(guarded_input, packet_dir=report.packet_dir)
        for guarded_input in report.guarded_inputs
    )


def render_resolution_section(frontmatter: dict[str, Any]) -> str:
    """Render the canonical human-readable projection of resolution fields."""

    def display(field: str) -> str:
        value = frontmatter.get(field)
        return "—" if value is None else str(value)

    paths = frontmatter.get("resulting_paths")
    if isinstance(paths, list) and paths:
        rendered_paths = ", ".join(f"`{path}`" for path in paths)
    else:
        rendered_paths = "—"
    return (
        "## Resolution\n\n"
        f"**Status:** {display('resolution')}\n"
        f"**Resolved at:** {display('resolved_at')}\n"
        f"**Authority:** {display('resolution_authority')}\n"
        f"**Outcome:** {display('resolution_summary')}\n"
        f"**Rationale:** {display('resolution_rationale')}\n"
        f"**Resulting paths:** {rendered_paths}"
    )


def resolution_section(body: str) -> str | None:
    match = _RESOLUTION_HEADING_RE.search(body)
    if match is None:
        return None
    next_heading = _NEXT_H2_RE.search(body, match.end())
    end = next_heading.start() if next_heading is not None else len(body)
    return body[match.start() : end].strip()
