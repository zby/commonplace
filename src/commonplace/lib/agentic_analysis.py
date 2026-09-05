"""Minimal completion checks for rerunnable agentic-system analyses."""

from __future__ import annotations

import re
import subprocess
from collections.abc import Mapping
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import unquote, urlsplit

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
_GITHUB_URL_RE = re.compile(
    r"https?://github\.com/[^\s<>()`\"']+", re.IGNORECASE
)
_QUOTE_CITE_ATTR_RE = re.compile(r"^\s*>\s*---\s*(?P<attribution>.*\S)?\s*$")
_LOCAL_QUOTE_SOURCE_RE = re.compile(
    r"`(?P<path>[A-Za-z0-9._/-]+\.[A-Za-z0-9._-]+)"
    r"(?::(?P<ranges>[0-9]+(?:-[0-9]+)?(?:,[0-9]+(?:-[0-9]+)?)*)?)?`"
    r"\s*@\s*`(?P<revision>[^`]+)`"
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
            len(pure.parts) != 4
            or pure.parts[:3] != ("kb", "agentic-systems", "reviews")
            or pure.suffix != ".md"
        ):
            raise ValueError(
                "generated-review.path: expected "
                "kb/agentic-systems/reviews/<name>.md"
            )
    if status == "running":
        if any(
            item is not None
            for item in (
                result_disposition,
                result,
                generated_review,
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
            )
        ):
            raise ValueError("failed state cannot record completed outputs")
    else:
        if result_disposition not in {"complete", "blocked", "out-of-scope"}:
            raise ValueError("complete state requires a result disposition")
        if result is None or failure is not None:
            raise ValueError("complete state requires result and no failure")
        if result_disposition == "complete":
            if source is None or generated_review is None:
                raise ValueError(
                    "a complete analysis requires frozen source and generated review"
                )
        elif generated_review is not None:
            raise ValueError(
                "blocked and out-of-scope results cannot publish generated reviews"
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
        failure=failure,
    )


def _text_override(
    path: Path, content_overrides: Mapping[Path, str] | None
) -> str | None:
    if content_overrides is None:
        return None
    return content_overrides.get(path.resolve())


def _read_output_bytes(
    identity: OutputIdentity, content_overrides: Mapping[Path, str] | None
) -> bytes:
    override = _text_override(identity.path, content_overrides)
    if override is not None:
        return override.encode("utf-8")
    return identity.path.read_bytes()


def _read_output_text(
    identity: OutputIdentity, content_overrides: Mapping[Path, str] | None
) -> str:
    override = _text_override(identity.path, content_overrides)
    if override is not None:
        return override
    return identity.path.read_text(encoding="utf-8")


def _verify_output(
    identity: OutputIdentity,
    content_overrides: Mapping[Path, str] | None,
) -> str | None:
    try:
        content = _read_output_bytes(identity, content_overrides)
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


def _git_blob_text(
    *, source_root: Path, revision: str, source_path: str
) -> tuple[str | None, str | None]:
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
                "cat-file",
                "blob",
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
    return content, None


def _git_blob_lines(
    *, source_root: Path, revision: str, source_path: str
) -> tuple[int | None, str | None]:
    content, error = _git_blob_text(
        source_root=source_root,
        revision=revision,
        source_path=source_path,
    )
    if error is not None or content is None:
        return None, error
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
    content: str, *, source_root: Path, source_identity: str, source_revision: str
) -> tuple[list[str], list[str]]:
    passes: list[str] = []
    failures: list[str] = []
    anchors: dict[tuple[str, tuple[tuple[int, int], ...]], set[str]] = {}

    for match in _LOCAL_SOURCE_ANCHOR_RE.finditer(content):
        key = (match.group("path"), _parse_line_ranges(match.group("ranges")))
        anchors.setdefault(key, set()).add("local")
    for match in _GITHUB_URL_RE.finditer(content):
        url = match.group().rstrip(".,;")
        parsed = urlsplit(url)
        parts = parsed.path.split("/")
        if len(parts) < 4 or parts[3] != "blob":
            continue
        if len(parts) < 6 or not parts[5]:
            failures.append(f"source citation: incomplete GitHub blob path: {url}")
            continue
        repository = f"https://github.com/{parts[1]}/{parts[2]}"
        expected_repository = source_identity.rstrip("/").removesuffix(".git")
        if repository.casefold() != expected_repository.casefold():
            failures.append(
                "source citation: GitHub anchor uses repository "
                f"{repository}, expected {source_identity}"
            )
            continue
        revision = parts[4]
        source_path = unquote("/".join(parts[5:]))
        if revision != source_revision:
            failures.append(
                "source citation: GitHub anchor uses revision "
                f"{revision}, expected {source_revision}: {source_path}"
            )
            continue
        line_ranges: tuple[tuple[int, int], ...] = ()
        if parsed.fragment:
            lines = re.fullmatch(r"L([0-9]+)(?:-L([0-9]+))?", parsed.fragment)
            if lines is None:
                failures.append(f"source citation: invalid GitHub line anchor: {url}")
                continue
            start = int(lines[1])
            end = int(lines[2] or start)
            line_ranges = ((start, end),)
        anchors.setdefault((source_path, line_ranges), set()).add("GitHub")

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


def _quote_citations(content: str) -> tuple[tuple[int, str, str], ...]:
    """Return attribution-line number, quote body, and attribution."""
    lines = content.splitlines()
    citations: list[tuple[int, str, str]] = []
    for index, line in enumerate(lines):
        match = _QUOTE_CITE_ATTR_RE.fullmatch(line)
        if match is None:
            continue
        quote_lines: list[str] = []
        cursor = index - 1
        while cursor >= 0 and re.match(r"^\s*>", lines[cursor]):
            quote_lines.append(re.sub(r"^\s*> ?", "", lines[cursor], count=1))
            cursor -= 1
        citations.append(
            (
                index + 1,
                "\n".join(reversed(quote_lines)).strip(),
                (match.group("attribution") or "").strip(),
            )
        )
    return tuple(citations)


def _normalized_whitespace(value: str) -> str:
    return " ".join(value.split())


def _github_quote_source(
    attribution: str, *, source_identity: str, source_revision: str
) -> tuple[str | None, str | None]:
    match = _GITHUB_URL_RE.search(attribution)
    if match is None:
        return None, None
    url = match.group().rstrip(".,;")
    parsed = urlsplit(url)
    parts = parsed.path.split("/")
    if len(parts) < 6 or parts[3] != "blob" or not parts[5]:
        return None, f"incomplete GitHub blob path: {url}"
    repository = f"https://github.com/{parts[1]}/{parts[2]}"
    expected_repository = source_identity.rstrip("/").removesuffix(".git")
    if repository.casefold() != expected_repository.casefold():
        return None, (
            f"GitHub attribution uses repository {repository}, "
            f"expected {source_identity}"
        )
    revision = parts[4]
    if revision != source_revision:
        return None, (
            f"GitHub attribution uses revision {revision}, "
            f"expected {source_revision}"
        )
    return unquote("/".join(parts[5:])), None


def _local_quote_source(
    attribution: str, *, source_revision: str
) -> tuple[str | None, str | None]:
    match = _LOCAL_QUOTE_SOURCE_RE.search(attribution)
    if match is None:
        return None, (
            "expected a commit-pinned GitHub blob URL or "
            "`commit-relative/path` @ `full-commit`"
        )
    revision = match.group("revision")
    if revision != source_revision:
        return None, (
            f"local attribution uses revision {revision}, "
            f"expected {source_revision}"
        )
    return match.group("path"), None


def _verify_quote_anchors(
    content: str, *, source: SourceIdentity
) -> tuple[list[str], list[str]]:
    """Resolve quote-anchored citations against one frozen source."""
    passes: list[str] = []
    failures: list[str] = []
    citations = _quote_citations(content)
    if not citations:
        return passes, failures

    capture_text: str | None = None
    capture_error: str | None = None
    if source.kind == "capture":
        try:
            capture_bytes = source.path.read_bytes()
            actual_sha256 = sha256(capture_bytes).hexdigest()
            if actual_sha256 != source.expected_sha256:
                capture_error = (
                    "frozen capture SHA-256 mismatch; expected "
                    f"{source.expected_sha256}, got {actual_sha256}"
                )
            else:
                capture_text = capture_bytes.decode("utf-8")
        except (OSError, UnicodeError) as exc:
            capture_error = f"cannot read frozen capture as UTF-8 text: {exc}"

    for line_number, quote, attribution in citations:
        label = f"quote-anchored citation at output line {line_number}"
        if not quote:
            failures.append(f"{label}: quote body is empty")
            continue
        if not attribution:
            failures.append(f"{label}: attribution is empty")
            continue

        if source.kind == "capture":
            source_text, error = capture_text, capture_error
            location = f"frozen capture {source.revision}"
        else:
            source_path, error = _github_quote_source(
                attribution,
                source_identity=source.identity,
                source_revision=source.revision,
            )
            if source_path is None and error is None:
                source_path, error = _local_quote_source(
                    attribution, source_revision=source.revision
                )
            if error is not None or source_path is None:
                failures.append(f"{label}: {error}")
                continue
            source_text, error = _git_blob_text(
                source_root=source.path,
                revision=source.revision,
                source_path=source_path,
            )
            location = f"{source_path} at the recorded commit"

        if error is not None or source_text is None:
            failures.append(f"{label}: {error}")
            continue
        if _normalized_whitespace(quote) not in _normalized_whitespace(source_text):
            failures.append(f"{label}: quote does not occur in {location}")
            continue
        passes.append(f"{label}: quote resolves in {location}")
    return passes, failures


def _parsed_output(
    identity: OutputIdentity,
    content_overrides: Mapping[Path, str] | None,
) -> tuple[ParsedDocument | None, str | None]:
    try:
        content = _read_output_text(identity, content_overrides)
    except (OSError, UnicodeError) as exc:
        return None, str(exc)
    document, error = parse_document(content)
    if error is not None or document is None or document.frontmatter is None:
        return None, "frontmatter is not parseable"
    return document, None


def _parsed_frontmatter(
    identity: OutputIdentity,
    content_overrides: Mapping[Path, str] | None,
) -> tuple[dict[str, Any] | None, str | None]:
    document, error = _parsed_output(identity, content_overrides)
    if error is not None or document is None:
        return None, error
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
            f"**Run status:** {state.status}",
        ]
    )


def _run_identity_value(body: str, label: str) -> str | None:
    match = re.search(rf"(?m)^\*\*{re.escape(label)}:\*\*\s+(.+?)\s*$", body)
    if match is None:
        return None
    value = match.group(1).strip()
    if value.startswith("`") and value.endswith("`"):
        value = value[1:-1]
    return value


def _verify_result_projection_paths(
    state: AgenticAnalysisRunState,
    result_document: ParsedDocument,
) -> tuple[list[str], list[str]]:
    expected = {
        "Run state": state.path.relative_to(state.repo_root).as_posix(),
        "Generated review": (
            state.generated_review.display_path
            if state.generated_review is not None
            else "not applicable"
        ),
    }
    failures: list[str] = []
    for label, expected_value in expected.items():
        actual = _run_identity_value(result_document.body, label)
        if actual != expected_value:
            failures.append(
                f"result: {label.lower()} projection is {actual!r}, "
                f"expected {expected_value!r}"
            )
    if failures:
        return [], failures
    return ["result: intended publication paths match run state"], []


def _verify_memory_report(
    state: AgenticAnalysisRunState, result_document: ParsedDocument,
) -> tuple[list[str], list[str]]:
    """Check the specialist's retained handoff without certifying its conclusions."""
    from commonplace.lib import validation as validation_lib

    report_path = state.run_dir / "memory-report.md"
    expected_path = report_path.relative_to(state.repo_root).as_posix()
    if _run_identity_value(result_document.body, "Memory analysis report") != expected_path:
        return [], ["memory report: result must identify this run's memory-report.md"]
    try:
        report_bytes = report_path.read_bytes()
        input_bytes = (state.run_dir / "memory-input.md").read_bytes()
        document, error = parse_document(report_bytes.decode("utf-8"))
        if error or document is None:
            raise ValueError(error or "missing document")
    except (OSError, UnicodeError, ValueError) as exc:
        return [], [f"memory report: cannot read report or frozen input: {exc}"]
    failures = []
    if _run_identity_value(result_document.body, "Memory analysis report SHA-256") != sha256(report_bytes).hexdigest():
        failures.append("memory report: result's report SHA-256 does not match exact report bytes")
    expected = {
        "type": "kb/reports/types/agent-memory-analysis-report.md",
        "analysis-run": state.run_id,
        "source-identity": None if state.source is None else state.source.identity,
        "reviewed-boundary": None if state.source is None else state.source.revision,
        "report-status": "complete",
        "canonical-register-sha256": sha256(input_bytes).hexdigest(),
    }
    actual = document.frontmatter or {}
    for field, value in expected.items():
        if actual.get(field) != value:
            failures.append(f"memory report: {field} does not match completed run handoff")
    checks = validation_lib.validate_note(report_path, repo_root=state.repo_root)
    failures.extend(f"memory report validation: {message}" for message in (*checks.warns, *checks.fails))
    if state.source is not None:
        content = report_bytes.decode("utf-8")
        if state.source.kind == "git":
            _, errors = _verify_source_anchors(
                content, source_root=state.source.path,
                source_identity=state.source.identity,
                source_revision=state.source.revision,
            )
            failures.extend(f"memory report: {error}" for error in errors)
        _, errors = _verify_quote_anchors(content, source=state.source)
        failures.extend(f"memory report: {error}" for error in errors)
    if failures:
        return [], failures
    return ["memory report: typed report, frozen input, and integration byte identities match"], []


def verify_agentic_analysis_run_state(
    state: AgenticAnalysisRunState,
    *,
    content_overrides: Mapping[Path, str] | None = None,
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
        for item in (state.result, state.generated_review)
        if item is not None
    )
    for output in outputs:
        error = _verify_output(output, content_overrides)
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
        override = _text_override(output.path, content_overrides)
        checked = (
            validation_lib.validate_note_text_at_path(
                override,
                path=output.path,
                repo_root=state.repo_root,
                content_overrides=dict(content_overrides or {}),
            )
            if override is not None
            else validation_lib.validate_note(output.path, repo_root=state.repo_root)
        )
        diagnostics = [*checked.warns, *checked.fails]
        if diagnostics:
            failures.extend(
                f"{output.role} validation: {diagnostic}"
                for diagnostic in diagnostics
            )
        else:
            passes.append(f"{output.role}: direct validation passed")

    result_document, error = _parsed_output(state.result, content_overrides)
    if error is not None or result_document is None:
        failures.append(f"result: {error}")
        return passes, failures
    result_frontmatter = result_document.frontmatter
    assert result_frontmatter is not None
    if state.result_disposition == "complete":
        report_passes, report_failures = _verify_memory_report(state, result_document)
        passes.extend(report_passes)
        failures.extend(report_failures)
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
    projection_passes, projection_failures = _verify_result_projection_paths(
        state, result_document
    )
    passes.extend(projection_passes)
    failures.extend(projection_failures)

    if state.generated_review is not None:
        from commonplace.lib.systems_matrix import retained_result_path

        retained_relative = retained_result_path(state.run_id)
        retained = OutputIdentity(
            role="retained result",
            display_path=retained_relative.as_posix(),
            path=state.repo_root / retained_relative,
            expected_sha256=state.result.expected_sha256,
        )
        retained_error = _verify_output(retained, content_overrides)
        if retained_error:
            failures.append(retained_error)
        else:
            passes.append("retained result: exact result bytes preserved")
        generated_frontmatter, error = _parsed_frontmatter(
            state.generated_review, content_overrides
        )
        if error is not None or generated_frontmatter is None:
            failures.append(f"generated review: {error}")
        else:
            expected = {
                "type": "kb/types/note.md",
                "generated-by": "analyse-agentic-system",
                "analysis-run": state.run_id,
                "source-identity": None if state.source is None else state.source.identity,
                "reviewed-revision": None if state.source is None else state.source.revision,
                "analysis-result": retained_relative.as_posix(),
                "analysis-result-sha256": state.result.expected_sha256,
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

    if state.source is not None:
        for output in outputs:
            try:
                content = _read_output_text(output, content_overrides)
            except (OSError, UnicodeError):
                continue
            if state.source.kind == "git":
                anchor_passes, anchor_failures = _verify_source_anchors(
                    content,
                    source_root=state.source.path,
                    source_identity=state.source.identity,
                    source_revision=state.source.revision,
                )
                passes.extend(anchor_passes)
                failures.extend(anchor_failures)
            quote_passes, quote_failures = _verify_quote_anchors(
                content, source=state.source
            )
            passes.extend(f"{output.role} {message}" for message in quote_passes)
            failures.extend(f"{output.role} {message}" for message in quote_failures)

    return passes, failures
