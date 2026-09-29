"""Minimal completion checks for rerunnable agentic-system analyses."""

from __future__ import annotations

import subprocess
from collections.abc import Mapping
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path, PurePosixPath
from typing import Any

from commonplace.lib.agentic_set import (
    MANIFEST_NAME,
    OUTPUT_DIR,
    OVERVIEW_NAME,
    REVIEW_TYPE,
    SET_NAMES,
    is_normalized_relative,
    is_review_path,
    load_member_set,
    normalize_source_identity,
    retained_set_paths,
)
from commonplace.lib.note_parser import ParsedDocument, parse_document
from commonplace.lib.quote_matching import (
    URL_RE,
    blank_quote_bodies,
    git_citation_path,
    match_quote,
    parse_blockquotes,
    parse_github_blob,
)

AGENTIC_ANALYSIS_RUN_TYPE = "types/agentic-system-analysis-run-state.md"



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
    artifact: OutputIdentity | None
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


def _repo_relative_file(value: str, *, repo_root: Path, field: str) -> Path:
    if not is_normalized_relative(value) or PurePosixPath(value).parts[0] != "kb":
        raise ValueError(f"{field}: expected a normalized repository-relative kb/ path")
    candidate = repo_root / value
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
    source_path = Path(_required_string(value, "path"))
    if not source_path.is_absolute():
        raise ValueError("source.path: expected an absolute path")
    return SourceIdentity(
        kind=_required_string(value, "kind"),
        identity=_required_string(value, "identity"),
        revision=_required_string(value, "revision"),
        path=source_path,
        expected_sha256=_optional_string(value, "sha256"),
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
        expected_sha256=_required_string(value, "sha256"),
    )


def parse_agentic_analysis_run_state(
    path: Path,
    document: ParsedDocument,
    *,
    repo_root: Path,
) -> AgenticAnalysisRunState:
    """Extract the fields of one run-state record.

    The run-state schema owns field values and their consistency across
    statuses; callers validate the record with ``validate_note`` first, or
    this runs inside that validation. What is checked here is what the schema
    cannot express: the record's location and the paths it names.
    """
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

    result_disposition = _optional_string(frontmatter, "result-disposition")
    source = _source_identity(frontmatter.get("source"))
    artifact = _output_identity(
        frontmatter.get("artifact"), role="artifact", repo_root=repo_root
    )
    generated_review = _output_identity(
        frontmatter.get("generated-review"),
        role="generated review",
        repo_root=repo_root,
    )
    failure = _optional_string(frontmatter, "failure")

    expected_artifact = (state_root / run_id / OUTPUT_DIR / MANIFEST_NAME).resolve()
    if artifact is not None and artifact.path.resolve() != expected_artifact:
        raise ValueError(f"artifact.path: expected <run-id>/{OUTPUT_DIR}/{MANIFEST_NAME}")
    if generated_review is not None and not is_review_path(generated_review.display_path):
        raise ValueError("generated-review.path: expected kb/agentic-systems/reviews/<name>.md")
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
        artifact=artifact,
        generated_review=generated_review,
        failure=failure,
    )


def run_state_repo_root(path: Path) -> Path | None:
    """The repository whose analysis state directory holds this run state, or
    None when the path is not in one."""
    parents = path.parents
    if len(parents) < 6:
        return None
    root = parents[5]
    if path.parent.parent != root / "kb" / "reports" / "state" / "agentic-system-analysis":
        return None
    return root


def load_run_state(path: Path, *, repo_root: Path) -> AgenticAnalysisRunState:
    """Validate one run-state record, then return its fields.

    Any validation warning or failure raises ``ValueError``.
    """
    # Import lazily because validation registers this module's type rule.
    from commonplace.lib import validation

    if not path.is_file():
        raise ValueError(f"run state does not exist: {path}")
    results = validation.validate_note(path, repo_root=repo_root)
    diagnostics = [*results.warns, *results.fails]
    if diagnostics:
        raise ValueError("run-state validation failed: " + "; ".join(diagnostics))
    try:
        content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise ValueError(f"cannot read run state {path}: {exc}") from exc
    document, error = parse_document(content)
    if error is not None or document is None:
        raise ValueError("run state is not parseable")
    return parse_agentic_analysis_run_state(path, document, repo_root=repo_root)


def _text_override(
    path: Path, content_overrides: Mapping[Path, str | bytes] | None
) -> str | None:
    if content_overrides is None:
        return None
    value = content_overrides.get(path.resolve())
    return value.decode("utf-8") if isinstance(value, bytes) else value


def _read_output_bytes(
    identity: OutputIdentity, content_overrides: Mapping[Path, str | bytes] | None
) -> bytes:
    override = _text_override(identity.path, content_overrides)
    if override is not None:
        return override.encode("utf-8")
    return identity.path.read_bytes()


def _read_output_text(
    identity: OutputIdentity, content_overrides: Mapping[Path, str | bytes] | None
) -> str:
    override = _text_override(identity.path, content_overrides)
    if override is not None:
        return override
    return identity.path.read_text(encoding="utf-8")


def _verify_output(
    identity: OutputIdentity,
    content_overrides: Mapping[Path, str | bytes] | None,
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


def _read_capture(source: SourceIdentity) -> tuple[bytes | None, str | None]:
    """Return the frozen capture's bytes, or an error, after checking their hash."""
    try:
        content = source.path.read_bytes()
    except OSError as exc:
        return None, f"cannot read frozen capture {source.path}: {exc}"
    actual = sha256(content).hexdigest()
    if actual != source.expected_sha256:
        return None, (
            f"frozen capture SHA-256 mismatch; expected {source.expected_sha256}, "
            f"got {actual}"
        )
    return content, None


def _verify_git_source(source: SourceIdentity) -> str | None:
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


def git_blob_text(
    *, source_root: Path, revision: str, source_path: str
) -> tuple[str | None, str | None]:
    if not is_normalized_relative(source_path):
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


def _same_repository(repository: str, source_identity: str) -> bool:
    expected = normalize_source_identity(source_identity)
    return repository.casefold() == expected.casefold()


def _git_blob_exists(
    *, source_root: Path, revision: str, source_path: str
) -> str | None:
    """Check that a path names a blob at the commit, without decoding it."""
    if not is_normalized_relative(source_path):
        return "expected a normalized commit-relative path"
    try:
        kind = subprocess.run(
            [
                "git",
                "--no-replace-objects",
                "-C",
                str(source_root),
                "cat-file",
                "-t",
                f"{revision}:{source_path}",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError as exc:
        return f"could not invoke git: {exc}"
    if kind.returncode != 0 or kind.stdout.strip() != "blob":
        return "path does not resolve to a blob at the recorded commit"
    return None


def _verify_source_anchors(
    content: str, *, source_root: Path, source_identity: str, source_revision: str
) -> tuple[list[str], list[str]]:
    """Resolve GitHub source links by path at the recorded commit.

    Line ranges belong to quote attributions, which quote verification
    resolves; member validation rejects ranged anchors in prose. A cited
    path only has to exist, so a binary blob can be cited.
    """
    content = blank_quote_bodies(content)
    passes: list[str] = []
    failures: list[str] = []
    paths: set[str] = set()

    for match in URL_RE.finditer(content):
        url = match.group().rstrip(".,;")
        try:
            blob = parse_github_blob(url)
        except ValueError as exc:
            failures.append(f"source citation: {exc}: {url}")
            continue
        if blob is None:
            continue
        if not _same_repository(blob.repository, source_identity):
            failures.append(
                "source citation: GitHub anchor uses repository "
                f"{blob.repository}, expected {source_identity}"
            )
            continue
        if blob.revision != source_revision:
            failures.append(
                "source citation: GitHub anchor uses revision "
                f"{blob.revision}, expected {source_revision}: {blob.path}"
            )
            continue
        paths.add(blob.path)

    for source_path in sorted(paths):
        error = _git_blob_exists(
            source_root=source_root,
            revision=source_revision,
            source_path=source_path,
        )
        if error is not None:
            failures.append(f"source citation: {source_path}: {error}")
            continue
        passes.append(
            f"source citation: {source_path} resolves at the recorded commit (GitHub)"
        )
    return passes, failures


def verify_quote_anchors(
    content: str,
    *,
    source: SourceIdentity,
    capture: tuple[bytes | None, str | None] | None = None,
) -> tuple[list[str], list[str]]:
    """Resolve quote-anchored citations against one frozen source.

    ``capture`` is a capture source's already verified ``(bytes, error)``, so
    a caller checking several documents reads and hashes the capture once.
    """
    passes: list[str] = []
    failures: list[str] = []
    citations = parse_blockquotes(content)
    if not citations:
        return passes, failures

    capture_text: str | None = None
    capture_error: str | None = None
    if source.kind == "capture":
        capture_bytes, capture_error = capture or _read_capture(source)
        if capture_bytes is not None:
            try:
                capture_text = capture_bytes.decode("utf-8")
            except UnicodeError as exc:
                capture_error = f"cannot read frozen capture as UTF-8 text: {exc}"

    for citation in citations:
        label = f"quote-anchored citation at output line {citation.line}"
        if not citation.quote.strip():
            failures.append(f"{label}: quote body is empty")
            continue
        if citation.error:
            failures.append(f"{label}: source error: {citation.error}")
            continue
        if source.kind == "capture":
            source_text, error = capture_text, capture_error
            location = f"frozen capture {source.revision}"
            if citation.source and citation.source.startswith(("http://", "https://")):
                if citation.source != source.identity:
                    error = "attribution URL does not match registered capture identity; cite its pinned capture path"
                elif citation.ranges:
                    error = "a blob line range cannot address the full capture; cite a capture range"
            elif citation.version is not None:
                if citation.version != f"sha256:{source.expected_sha256}":
                    error = "attribution checksum does not match frozen capture"
                elif Path(citation.source or "").as_posix() != source.path.as_posix() and not source.path.as_posix().endswith("/" + (citation.source or "")):
                    error = "attribution path does not identify frozen capture"
        else:
            try:
                source_path, repository = git_citation_path(citation)
            except ValueError as exc:
                failures.append(f"{label}: source error: {exc}")
                continue
            if repository and not _same_repository(repository, source.identity):
                failures.append(f"{label}: source error: attribution uses repository {repository}, expected {source.identity}")
                continue
            if citation.version != source.revision:
                failures.append(f"{label}: source error: attribution uses revision {citation.version}, expected {source.revision}")
                continue
            source_text, error = git_blob_text(
                source_root=source.path, revision=source.revision, source_path=source_path,
            )
            location = f"{source_path} at the recorded commit"
        if error is not None or source_text is None:
            failures.append(f"{label}: source error: {error}")
            continue
        matched = match_quote(citation.quote, source_text, kind="code", ranges=citation.ranges)
        if not matched.matched:
            failures.append(f"{label}: {matched.error} ({location})")
            continue
        passes.append(f"{label}: quote resolves in {location}")
    return passes, failures


def _parsed_output(
    identity: OutputIdentity,
    content_overrides: Mapping[Path, str | bytes] | None,
) -> tuple[ParsedDocument | None, str | None]:
    try:
        content = _read_output_text(identity, content_overrides)
    except (OSError, UnicodeError) as exc:
        return None, str(exc)
    document, error = parse_document(content)
    if error is not None or document is None or document.frontmatter is None:
        return None, "frontmatter is not parseable"
    return document, None


def render_agentic_analysis_handoff(state: AgenticAnalysisRunState) -> str:
    """Render the operator handoff for one completed run."""
    if state.status != "complete" or state.artifact is None:
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
    members = (
        ", ".join(SET_NAMES) + " (pinned by ARTIFACT.yaml)"
        if state.result_disposition == "complete"
        else "none"
    )
    return "\n".join(
        [
            f"# Agentic-system analysis handoff — {state.run_id}",
            "",
            f"**Artifact:** [{state.artifact.display_path}](<{state.artifact.path.as_posix()}>)",
            "",
            f"**Members:** {members}",
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


def verify_agentic_analysis_run_state(
    state: AgenticAnalysisRunState,
    *,
    run,
) -> tuple[list[str], list[str]]:
    """Verify the frozen source and exact bytes named by the state."""
    # All workflow reads use the same snapshot as member validation.
    content_overrides = run._bytes
    passes: list[str] = []
    failures: list[str] = []

    capture = None
    if state.source is not None:
        if state.source.kind == "capture":
            capture = _read_capture(state.source)
            error = None if capture[1] is None else f"source capture: {capture[1]}"
        else:
            error = _verify_git_source(state.source)
        if error is None:
            passes.append(
                f"source: {state.source.identity} resolves at {state.source.revision}"
            )
        else:
            failures.append(error)

    outputs = tuple(
        item
        for item in (state.artifact, state.generated_review)
        if item is not None
    )
    for output in outputs:
        try:
            run.read_bytes(output.path)
        except OSError:
            pass
        error = _verify_output(output, content_overrides)
        if error is None:
            passes.append(f"{output.role}: byte identity matches {output.display_path}")
        else:
            failures.append(error)

    if state.status != "complete" or state.artifact is None:
        return passes, failures

    if state.generated_review is not None:
        checked = run.validate(state.generated_review.path)
        failures.extend(f"generated review validation: {error}" for error in [*checked.fails, *checked.warns])
    try:
        member_set = load_member_set(state.artifact.path.parent, run=run)
    except ValueError as exc:
        failures.append(f"member set: {exc}")
        return passes, failures
    overview_frontmatter = member_set.overview.frontmatter
    if overview_frontmatter.get("run-id") != state.run_id:
        failures.append("overview: run-id does not match run state")
    if overview_frontmatter.get("system") != state.system:
        failures.append("overview: system does not match run state")
    if overview_frontmatter.get("result-disposition") != state.result_disposition:
        failures.append("overview: disposition does not match run state")
    if state.source is not None and (
        overview_frontmatter.get("reviewed-boundary") != state.source.revision
    ):
        failures.append("overview: reviewed-boundary does not match frozen source")
    if not any(message.startswith("overview:") for message in failures):
        passes.append("overview: workflow identity matches run state")

    if state.result_disposition == "complete" and member_set.memory is not None:
        passes.append("member set: manifest members present, hashed and typed")
        if state.source is not None and member_set.memory.frontmatter.get("source-identity") != state.source.identity:
            failures.append("memory.md: source-identity does not match the frozen source")

    if state.generated_review is not None:
        retained_paths = retained_set_paths(state.run_id)
        expected_hashes = {MANIFEST_NAME: state.artifact.expected_sha256,
                           OVERVIEW_NAME: member_set.overview.sha256}
        expected_hashes.update(
            {name: member.sha256 for name, member in member_set.members.items()}
        )
        retained_failures = []
        for name, expected_sha256 in expected_hashes.items():
            retained = OutputIdentity(
                role=f"retained {name}",
                display_path=retained_paths[name].as_posix(),
                path=state.repo_root / retained_paths[name],
                expected_sha256=expected_sha256,
            )
            try:
                run.read_bytes(retained.path)
            except OSError:
                pass
            retained_error = _verify_output(retained, content_overrides)
            if retained_error:
                retained_failures.append(retained_error)
        if retained_failures:
            failures.extend(retained_failures)
        else:
            passes.append("retained set: exact member bytes preserved")
            try:
                load_member_set((state.repo_root / retained_paths[MANIFEST_NAME]).parent, run=run)
            except ValueError as exc:
                failures.append(f"retained artifact: {exc}")
        generated, error = _parsed_output(state.generated_review, content_overrides)
        if error is not None or generated is None:
            failures.append(f"generated review: {error}")
        else:
            generated_frontmatter = generated.frontmatter or {}
            expected = {
                "type": REVIEW_TYPE,
                "generated-by": "analyse-agentic-system",
                "analysis-run": state.run_id,
                "source-identity": None if state.source is None else state.source.identity,
                "reviewed-revision": None if state.source is None else state.source.revision,
                "analysis-artifact": retained_paths[MANIFEST_NAME].as_posix(),
                "analysis-artifact-sha256": state.artifact.expected_sha256,
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
        contents = [(document.name, document.text) for document in member_set.documents]
        if state.generated_review is not None:
            try:
                contents.append(
                    (state.generated_review.role, _read_output_text(state.generated_review, content_overrides))
                )
            except (OSError, UnicodeError):
                pass
        for role, content in contents:
            if state.source.kind == "git":
                anchor_passes, anchor_failures = _verify_source_anchors(
                    content,
                    source_root=state.source.path,
                    source_identity=state.source.identity,
                    source_revision=state.source.revision,
                )
                passes.extend(f"{role} {message}" for message in anchor_passes)
                failures.extend(f"{role} {message}" for message in anchor_failures)
            quote_passes, quote_failures = verify_quote_anchors(
                content, source=state.source, capture=capture
            )
            passes.extend(f"{role} {message}" for message in quote_passes)
            failures.extend(f"{role} {message}" for message in quote_failures)

    return passes, failures
