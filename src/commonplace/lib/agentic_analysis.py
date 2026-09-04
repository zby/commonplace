"""Minimal completion checks for rerunnable agentic-system analyses."""

from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path, PurePosixPath
from typing import Any

from commonplace.lib.note_parser import ParsedDocument, parse_document

AGENTIC_ANALYSIS_RUN_TYPE = (
    "kb/reports/types/agentic-system-analysis-run-state.md"
)
AGENTIC_ANALYSIS_RESULT_TYPE = "kb/types/agentic-system-analysis-result.md"

_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
_LOCAL_SOURCE_ANCHOR_RE = re.compile(
    r"`(?P<path>[A-Za-z0-9._/-]+\.[A-Za-z0-9._-]+):"
    r"(?P<ranges>[0-9]+(?:-[0-9]+)?(?:,[0-9]+(?:-[0-9]+)?)*)`"
)
_GITHUB_BLOB_ANCHOR_RE = re.compile(
    r"https://github\.com/[^/\s)]+/[^/\s)]+/blob/"
    r"(?P<revision>[0-9a-f]{40}|[0-9a-f]{64})/"
    r"(?P<path>[^\s)#]+)#L(?P<start>[0-9]+)(?:-L(?P<end>[0-9]+))?"
)


@dataclass(frozen=True)
class SourceIdentity:
    kind: str
    identity: str
    revision: str
    path: Path
    expected_sha256: str | None


@dataclass(frozen=True)
class OutputIdentity:
    role: str
    display_path: str
    path: Path
    expected_sha256: str


@dataclass(frozen=True)
class AgenticAnalysisRunState:
    path: Path
    run_dir: Path
    repo_root: Path
    frontmatter: dict[str, Any]
    run_id: str
    system: str
    status: str
    result_disposition: str | None
    source: SourceIdentity | None
    result: OutputIdentity | None
    generated_review: OutputIdentity | None
    memory_review_required: bool | None
    legacy_review: OutputIdentity | None
    failure: str | None


def _required_string(values: dict[str, Any], field: str) -> str:
    value = values.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field}: expected a non-empty string")
    return value


def _optional_string(values: dict[str, Any], field: str) -> str | None:
    value = values.get(field)
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field}: expected null or a non-empty string")
    return value


def _required_sha256(values: dict[str, Any], field: str) -> str:
    value = _required_string(values, field)
    if not _SHA256_RE.fullmatch(value):
        raise ValueError(f"{field}: expected a lowercase SHA-256 hex digest")
    return value


def _repo_relative_file(value: str, *, repo_root: Path, field: str) -> Path:
    pure = PurePosixPath(value)
    if (
        pure.is_absolute()
        or value != pure.as_posix()
        or ".." in pure.parts
        or not pure.parts
        or pure.parts[0] != "kb"
    ):
        raise ValueError(f"{field}: expected a normalized repository-relative kb/ path")
    candidate = repo_root.joinpath(*pure.parts)
    try:
        candidate.resolve(strict=False).relative_to(repo_root.resolve())
    except ValueError as exc:
        raise ValueError(f"{field}: path escapes the repository") from exc
    return candidate


def _source_identity(value: Any) -> SourceIdentity | None:
    if value is None:
        return None
    if not isinstance(value, dict):
        raise ValueError("source: expected null or a mapping")  # noqa: TRY004
    kind = _required_string(value, "kind")
    if kind not in {"git", "capture"}:
        raise ValueError("source.kind: expected git or capture")
    identity = _required_string(value, "identity")
    revision = _required_string(value, "revision")
    source_path = Path(_required_string(value, "path"))
    if not source_path.is_absolute():
        raise ValueError("source.path: expected an absolute path")
    expected_sha256 = _optional_string(value, "sha256")
    if kind == "git":
        if not re.fullmatch(r"(?:[0-9a-f]{40}|[0-9a-f]{64})", revision):
            raise ValueError("source.revision: expected a full Git commit ID")
        if expected_sha256 is not None:
            raise ValueError("source.sha256: expected null for a Git source")
    else:
        if expected_sha256 is None or not _SHA256_RE.fullmatch(expected_sha256):
            raise ValueError("source.sha256: expected a capture SHA-256")
    return SourceIdentity(
        kind=kind,
        identity=identity,
        revision=revision,
        path=source_path,
        expected_sha256=expected_sha256,
    )


def _output_identity(
    value: Any,
    *,
    role: str,
    repo_root: Path,
) -> OutputIdentity | None:
    if value is None:
        return None
    if not isinstance(value, dict):
        raise ValueError(f"{role}: expected null or a mapping")  # noqa: TRY004
    display_path = _required_string(value, "path")
    return OutputIdentity(
        role=role,
        display_path=display_path,
        path=_repo_relative_file(display_path, repo_root=repo_root, field=f"{role}.path"),
        expected_sha256=_required_sha256(value, "sha256"),
    )


def parse_agentic_analysis_run_state(
    path: Path,
    document: ParsedDocument,
    *,
    repo_root: Path,
) -> AgenticAnalysisRunState:
    """Build the minimal checked view of one run-state record."""
    repo_root = repo_root.resolve()
    state_path = path.resolve()
    state_root = (
        repo_root / "kb" / "reports" / "state" / "agentic-system-analysis"
    ).resolve()
    try:
        relative = state_path.relative_to(state_root)
    except ValueError as exc:
        raise ValueError(
            "run-state path: expected kb/reports/state/agentic-system-analysis/"
            "<run-id>/run-state.md"
        ) from exc
    if len(relative.parts) != 2 or relative.name != "run-state.md":
        raise ValueError(
            "run-state path: expected kb/reports/state/agentic-system-analysis/"
            "<run-id>/run-state.md"
        )

    frontmatter = document.frontmatter
    if frontmatter is None:
        raise ValueError("run state: missing frontmatter")
    if frontmatter.get("type") != AGENTIC_ANALYSIS_RUN_TYPE:
        raise ValueError(f"type: expected {AGENTIC_ANALYSIS_RUN_TYPE}")

    run_id = _required_string(frontmatter, "run-id")
    if relative.parts[0] != run_id:
        raise ValueError("run-id: expected the run-state parent directory name")
    system = _required_string(frontmatter, "system")
    status = _required_string(frontmatter, "run-status")
    if status not in {"running", "complete", "failed"}:
        raise ValueError("run-status: expected running, complete, or failed")

    result_disposition = _optional_string(frontmatter, "result-disposition")
    source = _source_identity(frontmatter.get("source"))
    result = _output_identity(
        frontmatter.get("result"), role="result", repo_root=repo_root
    )
    generated_review = _output_identity(
        frontmatter.get("generated-review"),
        role="generated review",
        repo_root=repo_root,
    )
    legacy_review = _output_identity(
        frontmatter.get("legacy-review"),
        role="legacy review",
        repo_root=repo_root,
    )
    memory_review_required = frontmatter.get("memory-review-required")
    if memory_review_required is not None and not isinstance(
        memory_review_required, bool
    ):
        raise ValueError("memory-review-required: expected true, false, or null")
    failure = _optional_string(frontmatter, "failure")

    expected_result = (
        repo_root
        / "kb"
        / "reports"
        / "state"
        / "agentic-system-analysis"
        / run_id
        / "result.md"
    ).resolve()
    if result is not None and result.path.resolve() != expected_result:
        raise ValueError("result.path: expected <run-id>/result.md")
    if generated_review is not None:
        pure = PurePosixPath(generated_review.display_path)
        if (
            len(pure.parts) != 3
            or pure.parts[:2] != ("kb", "agentic-systems")
            or pure.suffix != ".md"
        ):
            raise ValueError("generated-review.path: expected kb/agentic-systems/<name>.md")
    if legacy_review is not None:
        pure = PurePosixPath(legacy_review.display_path)
        if (
            len(pure.parts) != 4
            or pure.parts[:2] != ("kb", "agent-memory-systems")
            or pure.parts[2] not in {"reviews", "lightweight"}
            or pure.suffix != ".md"
        ):
            raise ValueError(
                "legacy-review.path: expected kb/agent-memory-systems/"
                "{reviews|lightweight}/<name>.md"
            )

    if status == "running":
        if any(
            item is not None
            for item in (
                result_disposition,
                result,
                generated_review,
                memory_review_required,
                legacy_review,
                failure,
            )
        ):
            raise ValueError("running state cannot record completion or failure fields")
    elif status == "failed":
        if failure is None:
            raise ValueError("failed state requires failure")
        if any(
            item is not None
            for item in (
                result_disposition,
                result,
                generated_review,
                memory_review_required,
                legacy_review,
            )
        ):
            raise ValueError("failed state cannot record completed outputs")
    else:
        if result_disposition not in {"complete", "blocked", "out-of-scope"}:
            raise ValueError("complete state requires a result disposition")
        if result is None or memory_review_required is None or failure is not None:
            raise ValueError("complete state requires result and memory-review disposition")
        if result_disposition == "complete":
            if source is None or generated_review is None:
                raise ValueError(
                    "a complete analysis requires frozen source and generated review"
                )
        elif generated_review is not None or memory_review_required:
            raise ValueError(
                "blocked and out-of-scope results cannot publish generated reviews"
            )
        if memory_review_required != (legacy_review is not None):
            raise ValueError(
                "legacy review must be present exactly when memory review is required"
            )

    return AgenticAnalysisRunState(
        path=state_path,
        run_dir=state_path.parent,
        repo_root=repo_root,
        frontmatter=frontmatter,
        run_id=run_id,
        system=system,
        status=status,
        result_disposition=result_disposition,
        source=source,
        result=result,
        generated_review=generated_review,
        memory_review_required=memory_review_required,
        legacy_review=legacy_review,
        failure=failure,
    )


def _verify_output(identity: OutputIdentity) -> str | None:
    try:
        content = identity.path.read_bytes()
    except OSError as exc:
        return f"{identity.role}: cannot read {identity.display_path}: {exc}"
    actual = sha256(content).hexdigest()
    if actual != identity.expected_sha256:
        return (
            f"{identity.role}: SHA-256 mismatch for {identity.display_path}; "
            f"expected {identity.expected_sha256}, got {actual}"
        )
    return None


def _verify_source(source: SourceIdentity) -> str | None:
    if source.kind == "capture":
        try:
            content = source.path.read_bytes()
        except OSError as exc:
            return f"source capture: cannot read {source.path}: {exc}"
        actual = sha256(content).hexdigest()
        if actual != source.expected_sha256:
            return (
                f"source capture: SHA-256 mismatch; expected {source.expected_sha256}, "
                f"got {actual}"
            )
        return None

    if not source.path.is_dir():
        return f"source checkout: directory does not exist: {source.path}"
    try:
        check = subprocess.run(
            [
                "git",
                "--no-replace-objects",
                "-C",
                str(source.path),
                "cat-file",
                "-e",
                f"{source.revision}^{{commit}}",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError as exc:
        return f"source checkout: could not invoke git: {exc}"
    if check.returncode != 0:
        return "source checkout: recorded revision is not a commit in the checkout"
    return None


def _git_blob_lines(
    *, source_root: Path, revision: str, source_path: str
) -> tuple[int | None, str | None]:
    pure = PurePosixPath(source_path)
    if (
        pure.is_absolute()
        or source_path != pure.as_posix()
        or ".." in pure.parts
        or not pure.parts
    ):
        return None, "expected a normalized commit-relative path"
    try:
        blob = subprocess.run(
            [
                "git",
                "--no-replace-objects",
                "-C",
                str(source_root),
                "show",
                f"{revision}:{source_path}",
            ],
            check=False,
            capture_output=True,
        )
    except OSError as exc:
        return None, f"could not invoke git: {exc}"
    if blob.returncode != 0:
        return None, "path does not resolve to a blob at the recorded commit"
    try:
        content = blob.stdout.decode("utf-8")
    except UnicodeDecodeError:
        return None, "cited blob is not UTF-8 text"
    return len(content.splitlines()), None


def _parse_line_ranges(value: str) -> tuple[tuple[int, int], ...]:
    ranges: list[tuple[int, int]] = []
    for item in value.split(","):
        start_text, separator, end_text = item.partition("-")
        start = int(start_text)
        end = int(end_text) if separator else start
        ranges.append((start, end))
    return tuple(ranges)


def _verify_source_anchors(
    content: str, *, source_root: Path, source_revision: str
) -> tuple[list[str], list[str]]:
    passes: list[str] = []
    failures: list[str] = []
    anchors: dict[tuple[str, tuple[tuple[int, int], ...]], set[str]] = {}

    for match in _LOCAL_SOURCE_ANCHOR_RE.finditer(content):
        key = (match.group("path"), _parse_line_ranges(match.group("ranges")))
        anchors.setdefault(key, set()).add("local")
    for match in _GITHUB_BLOB_ANCHOR_RE.finditer(content):
        revision = match.group("revision")
        source_path = match.group("path")
        start = int(match.group("start"))
        end = int(match.group("end") or start)
        key = (source_path, ((start, end),))
        anchors.setdefault(key, set()).add("GitHub")
        if revision != source_revision:
            failures.append(
                "source citation: GitHub anchor uses revision "
                f"{revision}, expected {source_revision}: {source_path}"
            )

    for (source_path, line_ranges), kinds in sorted(anchors.items()):
        line_count, error = _git_blob_lines(
            source_root=source_root,
            revision=source_revision,
            source_path=source_path,
        )
        if error is not None or line_count is None:
            failures.append(f"source citation: {source_path}: {error}")
            continue
        invalid_ranges = [
            (start, end)
            for start, end in line_ranges
            if start < 1 or end < start or end > line_count
        ]
        if invalid_ranges:
            rendered = ", ".join(
                str(start) if start == end else f"{start}-{end}"
                for start, end in invalid_ranges
            )
            failures.append(
                f"source citation: {source_path}: line range {rendered} is outside "
                f"the recorded blob's 1-{line_count} lines"
            )
            continue
        passes.append(
            f"source citation: {source_path} and {len(line_ranges)} line range(s) "
            f"resolve at the recorded commit ({'/'.join(sorted(kinds))})"
        )
    return passes, failures


def _parsed_frontmatter(identity: OutputIdentity) -> tuple[dict[str, Any] | None, str | None]:
    try:
        content = identity.path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return None, str(exc)
    document, error = parse_document(content)
    if error is not None or document is None or document.frontmatter is None:
        return None, "frontmatter is not parseable"
    return document.frontmatter, None


def render_agentic_analysis_handoff(state: AgenticAnalysisRunState) -> str:
    """Render the operator handoff for one completed run."""
    if state.status != "complete" or state.result is None:
        raise ValueError("operator handoff requires a complete run state")
    generated = (
        state.generated_review.display_path
        if state.generated_review is not None
        else "not applicable"
    )
    legacy = (
        state.legacy_review.display_path
        if state.legacy_review is not None
        else "not applicable"
    )
    boundary = (
        "not established"
        if state.source is None
        else f"{state.source.identity} @ {state.source.revision}"
    )
    return "\n".join(
        [
            f"# Agentic-system analysis handoff — {state.run_id}",
            "",
            f"**Result:** [{state.result.display_path}](<{state.result.path.as_posix()}>)",
            "",
            f"**System and disposition:** {state.system} — {state.result_disposition}",
            "",
            f"**Frozen source:** {boundary}",
            "",
            f"**Generated system review:** {generated}",
            "",
            f"**Legacy memory review:** {legacy}",
            "",
            f"**Run status:** {state.status}",
        ]
    )


def verify_agentic_analysis_run_state(
    state: AgenticAnalysisRunState,
) -> tuple[list[str], list[str]]:
    """Verify the frozen source and exact bytes named by the state."""
    passes: list[str] = []
    failures: list[str] = []

    if state.source is not None:
        error = _verify_source(state.source)
        if error is None:
            passes.append(
                f"source: {state.source.identity} resolves at {state.source.revision}"
            )
        else:
            failures.append(error)

    outputs = tuple(
        item
        for item in (state.result, state.generated_review, state.legacy_review)
        if item is not None
    )
    for output in outputs:
        error = _verify_output(output)
        if error is None:
            passes.append(f"{output.role}: byte identity matches {output.display_path}")
        else:
            failures.append(error)

    if state.status != "complete" or state.result is None:
        return passes, failures

    # Import lazily because validation registers this module's type rule.
    from commonplace.lib import validation as validation_lib

    for output in outputs:
        if any(message.startswith(f"{output.role}:") for message in failures):
            continue
        checked = validation_lib.validate_note(output.path, repo_root=state.repo_root)
        diagnostics = [*checked.warns, *checked.fails]
        if diagnostics:
            failures.extend(
                f"{output.role} validation: {diagnostic}"
                for diagnostic in diagnostics
            )
        else:
            passes.append(f"{output.role}: direct validation passed")

    result_frontmatter, error = _parsed_frontmatter(state.result)
    if error is not None or result_frontmatter is None:
        failures.append(f"result: {error}")
        return passes, failures
    if result_frontmatter.get("type") != AGENTIC_ANALYSIS_RESULT_TYPE:
        failures.append(f"result: expected type {AGENTIC_ANALYSIS_RESULT_TYPE}")
    if result_frontmatter.get("run-id") != state.run_id:
        failures.append("result: run-id does not match run state")
    if result_frontmatter.get("system") != state.system:
        failures.append("result: system does not match run state")
    if result_frontmatter.get("result-disposition") != state.result_disposition:
        failures.append("result: disposition does not match run state")
    if state.source is not None and (
        result_frontmatter.get("reviewed-boundary") != state.source.revision
    ):
        failures.append("result: reviewed-boundary does not match frozen source")
    if not any(message.startswith("result:") for message in failures):
        passes.append("result: workflow identity matches run state")

    if state.generated_review is not None:
        generated_frontmatter, error = _parsed_frontmatter(state.generated_review)
        if error is not None or generated_frontmatter is None:
            failures.append(f"generated review: {error}")
        else:
            expected = {
                "type": "kb/types/note.md",
                "generated-by": "analyse-agentic-system",
                "analysis-run": state.run_id,
                "source-identity": None if state.source is None else state.source.identity,
                "reviewed-revision": None if state.source is None else state.source.revision,
            }
            mismatches = [
                field
                for field, value in expected.items()
                if generated_frontmatter.get(field) != value
            ]
            if mismatches:
                failures.append(
                    "generated review: workflow identity mismatch in "
                    + ", ".join(mismatches)
                )
            else:
                passes.append("generated review: workflow identity matches run state")

    if state.legacy_review is not None:
        legacy_frontmatter, error = _parsed_frontmatter(state.legacy_review)
        accepted_types = {
            "kb/agent-memory-systems/types/agent-memory-system-review.md",
            "../types/agent-memory-system-review.md",
        }
        if error is not None or legacy_frontmatter is None:
            failures.append(f"legacy review: {error}")
        elif legacy_frontmatter.get("type") not in accepted_types:
            failures.append("legacy review: expected agent-memory-system-review type")
        else:
            passes.append("legacy review: type matches the publication contract")

    if state.source is not None and state.source.kind == "git":
        for output in outputs:
            try:
                content = output.path.read_text(encoding="utf-8")
            except (OSError, UnicodeError):
                continue
            anchor_passes, anchor_failures = _verify_source_anchors(
                content,
                source_root=state.source.path,
                source_revision=state.source.revision,
            )
            passes.extend(anchor_passes)
            failures.extend(anchor_failures)

    return passes, failures
