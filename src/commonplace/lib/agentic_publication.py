"""Prepare and publish one agentic-analysis set and its review projection."""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass, field
from hashlib import sha256
from pathlib import Path, PurePosixPath

import yaml

from commonplace.lib import validation
from commonplace.lib.agentic_analysis import (
    AgenticAnalysisRunState,
    parse_agentic_analysis_run_state,
)
from commonplace.lib.agentic_set import (
    LOCAL_INPUT_NAME,
    LOCAL_REPORT_NAME,
    OVERVIEW_NAME,
    OVERVIEW_TYPE,
    SET_NAMES,
    MemberSet,
    load_member_set,
    retained_overview_path,
    retained_set_paths,
)
from commonplace.lib.note_parser import ParsedDocument, parse_document

INCUMBENT_REVIEW_NAME = "incumbent-review.md"

# The files whose tree at ``inputs-commit`` supplied the run's method. A run
# publishes only while HEAD leaves them unchanged since that commit.
METHOD_PATHS: tuple[str, ...] = (
    "src/commonplace/",
    "kb/instructions/analyse-agentic-system/",
    "kb/instructions/analyse-agent-memory.md",
    "kb/instructions/analyse-external-system-epistemic-architecture.md",
    "kb/types/agentic-system-analysis-overview.md",
    "kb/types/agentic-system-analysis-overview.schema.yaml",
    "kb/types/agentic-system-runtime-report.md",
    "kb/types/agentic-system-runtime-report.schema.yaml",
    "kb/types/agentic-system-epistemic-report.md",
    "kb/types/agentic-system-epistemic-report.schema.yaml",
    "kb/types/agent-memory-analysis-report.md",
    "kb/types/agent-memory-analysis-report.schema.yaml",
    "kb/types/agentic-system-analysis-run-state.md",
    "kb/types/agentic-system-analysis-run-state.schema.yaml",
    "kb/agentic-systems/types/generated-review.md",
    "kb/agentic-systems/types/generated-review.schema.yaml",
    # Every member schema references these.
    "kb/types/note.schema.yaml",
    "kb/types/note-base.schema.yaml",
)

# Untracked or modified files may sit here while a batch runs: a sibling run's
# publication that has not been committed yet.
OUTPUT_LOCATIONS: tuple[str, ...] = (
    "kb/agentic-systems/reviews/",
    "kb/reports/retained/agentic-system-analysis/",
)


def incumbent_copy_name(name: str) -> str:
    """The recovery copy of a replaced set document, kept in the new run."""
    return f"incumbent-{name}"


RESERVED_CANDIDATE_NAMES = frozenset(
    {
        *SET_NAMES,
        LOCAL_INPUT_NAME,
        LOCAL_REPORT_NAME,
        INCUMBENT_REVIEW_NAME,
        *(incumbent_copy_name(name) for name in SET_NAMES),
    }
)


@dataclass(frozen=True)
class PublicationSpec:
    repo_root: Path
    run_state_path: Path
    generated_candidate_path: Path
    generated_destination: str
    expected_incumbent_sha256: str


@dataclass(frozen=True)
class PreparedPublication:
    prepared: bool = True


@dataclass(frozen=True)
class PublishedPublication:
    generated_path: str
    retained_path: str
    cleanup_warnings: tuple[str, ...]


@dataclass(frozen=True)
class _Incumbent:
    review_bytes: bytes | None = None
    # Retained set documents of the incumbent's run, by set name.
    set_paths: dict[str, Path] = field(default_factory=dict)
    set_bytes: dict[str, bytes] = field(default_factory=dict)

    @property
    def digest(self) -> str:
        return "absent" if self.review_bytes is None else sha256(self.review_bytes).hexdigest()


@dataclass(frozen=True)
class _CheckedSet:
    spec: PublicationSpec
    final_state_text: str
    generated_bytes: bytes
    member_set: MemberSet
    retained_paths: dict[str, Path]
    incumbent: _Incumbent


class PublicationUncertainError(RuntimeError):
    """A publication failure whose rollback did not fully restore old bytes."""


def _repo_path(repo_root: Path, raw: Path) -> Path:
    path = raw if raw.is_absolute() else repo_root / raw
    resolved = path.resolve()
    try:
        resolved.relative_to(repo_root)
    except ValueError as exc:
        raise ValueError(f"path is outside the repository: {raw}") from exc
    return resolved


def _destination_path(repo_root: Path, raw: str) -> Path:
    pure = PurePosixPath(raw)
    if (
        pure.is_absolute()
        or raw != pure.as_posix()
        or ".." in pure.parts
        or pure.suffix != ".md"
        or len(pure.parts) != 4
        or pure.parts[:3] != ("kb", "agentic-systems", "reviews")
    ):
        raise ValueError(
            "publication destination must be kb/agentic-systems/reviews/<name>.md: "
            f"{raw}"
        )
    path = repo_root.joinpath(*pure.parts)
    if path.is_symlink() or path.resolve() != path:
        raise ValueError("publication destination must not traverse symlinks")
    return path


def _read_utf8(path: Path, *, label: str) -> tuple[bytes, str]:
    try:
        content = path.read_bytes()
        return content, content.decode("utf-8")
    except (OSError, UnicodeError) as exc:
        raise ValueError(f"cannot read {label} {path}: {exc}") from exc


def _parse(content: str, *, label: str) -> ParsedDocument:
    document, error = parse_document(content)
    if error is not None or document is None or document.frontmatter is None:
        raise ValueError(f"{label} is not a parseable typed Markdown artifact")
    return document


def _load_running_state(path: Path, *, repo_root: Path) -> tuple[AgenticAnalysisRunState, ParsedDocument]:
    if not path.is_file():
        raise ValueError(f"run state does not exist: {path}")
    results = validation.validate_note(path, repo_root=repo_root)
    diagnostics = [*results.warns, *results.fails]
    if diagnostics:
        raise ValueError("running run-state validation failed: " + "; ".join(diagnostics))
    _, content = _read_utf8(path, label="run state")
    document = _parse(content, label="run state")
    state = parse_agentic_analysis_run_state(path, document, repo_root=repo_root)
    if state.status != "running":
        raise ValueError("publication requires a running run state")
    if state.source is None:
        raise ValueError("publication requires a frozen source in the run state")
    return state, document


def _require_candidate_in_run(candidate: Path, state: AgenticAnalysisRunState) -> None:
    try:
        relative = candidate.relative_to(state.run_dir)
    except ValueError as exc:
        raise ValueError(f"candidate must be inside {state.run_dir}: {candidate}") from exc
    if not relative.parts or candidate == state.path or candidate.name in RESERVED_CANDIDATE_NAMES:
        raise ValueError(f"candidate path is reserved: {candidate}")


def _git(repo_root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            ["git", *args], cwd=repo_root, check=False,
            capture_output=True, text=True, timeout=30,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise ValueError(f"cannot run git {args[0]} in the repository") from exc


def _status_entries(porcelain: str) -> list[tuple[str, str]]:
    """Parse ``git status --porcelain -z`` into ``(code, path)`` pairs.

    A rename or copy entry is followed by its origin path, reported as a
    second entry with the same code so both sides are checked.
    """
    fields = porcelain.split("\0")
    entries: list[tuple[str, str]] = []
    index = 0
    while index < len(fields):
        field_text = fields[index]
        index += 1
        if len(field_text) < 4:
            continue
        code, path = field_text[:2], field_text[3:]
        entries.append((code, path))
        if code[0] in "RC" and index < len(fields):
            entries.append((code, fields[index]))
            index += 1
    return entries


def require_publishable_worktree(repo_root: Path) -> None:
    """Require a worktree clean outside the workflow's own output locations.

    Under an output location, an untracked file or an unstaged modification
    of a tracked file is allowed: a sibling run's uncommitted publication, new
    or replacing an existing review. Anywhere else no tracked file may be
    modified or staged, and no untracked file may sit under ``kb/``. Ignored
    paths never count.
    """
    status = _git(repo_root, "status", "--porcelain", "-z", "--untracked-files=all")
    if status.returncode != 0:
        raise ValueError("cannot inspect the repository's Git status")
    changed: list[str] = []
    untracked: list[str] = []
    for code, path in _status_entries(status.stdout):
        in_outputs = path.startswith(OUTPUT_LOCATIONS)
        if code == "??":
            if path.startswith("kb/") and not in_outputs:
                untracked.append(path)
        elif not (code == " M" and in_outputs):
            changed.append(path)
    problems = []
    if changed:
        problems.append("tracked files with local changes: " + ", ".join(sorted(changed)))
    if untracked:
        problems.append(
            "untracked files under kb/ outside the publication outputs: "
            + ", ".join(sorted(untracked))
        )
    if problems:
        raise ValueError(
            "publication requires a clean worktree outside its output locations; "
            + "; ".join(problems)
        )


def require_method_unchanged(repo_root: Path, inputs_commit: object) -> None:
    """Require HEAD to descend from ``inputs-commit`` with the method paths unchanged."""
    if not isinstance(inputs_commit, str) or not re.fullmatch(r"[0-9a-f]{40}", inputs_commit):
        raise ValueError("overview inputs-commit must be a full 40-hex commit")
    ancestry = _git(repo_root, "merge-base", "--is-ancestor", inputs_commit, "HEAD")
    if ancestry.returncode != 0:
        raise ValueError(
            f"overview inputs-commit {inputs_commit} is not a commit in this repository "
            "or not an ancestor of HEAD"
        )
    diff = _git(repo_root, "diff", "--name-only", inputs_commit, "HEAD", "--", *METHOD_PATHS)
    if diff.returncode != 0:
        raise ValueError("cannot compare the method paths against inputs-commit")
    changed = sorted(line for line in diff.stdout.splitlines() if line)
    if changed:
        raise ValueError(
            f"method paths changed since inputs-commit {inputs_commit}: " + ", ".join(changed)
        )


def running_package_root() -> Path:
    """The checkout whose ``src/commonplace`` supplies the running code.

    Commonplace is installed editable from one checkout; commands run inside
    a batch worktree still execute that checkout's source.
    """
    import commonplace

    return Path(commonplace.__file__).resolve().parents[2]


def require_running_package_unchanged(inputs_commit: str) -> None:
    """Require the executing package source to equal ``inputs-commit``.

    The method-path check compares the publishing tree's history; this check
    covers the code actually running, which may come from another checkout.
    """
    root = running_package_root()
    if not (root / ".git").exists():
        raise ValueError(
            f"running commonplace package is not a source checkout ({root}); "
            "cannot confirm it matches inputs-commit"
        )
    if _git(root, "cat-file", "-e", f"{inputs_commit}^{{commit}}").returncode != 0:
        raise ValueError(
            f"inputs-commit {inputs_commit} is unknown to the checkout running "
            f"commonplace ({root})"
        )
    changed = _git(root, "diff", "--name-only", inputs_commit, "--", "src/commonplace")
    untracked = _git(root, "ls-files", "--others", "--exclude-standard", "--", "src/commonplace")
    if changed.returncode != 0 or untracked.returncode != 0:
        raise ValueError("cannot compare the running package source against inputs-commit")
    paths = sorted({*changed.stdout.split(), *untracked.stdout.split()})
    if paths:
        raise ValueError(
            f"running commonplace source ({root}) differs from inputs-commit "
            f"{inputs_commit}: " + ", ".join(paths)
        )


def _check_incumbent(
    *, path: Path, repo_root: Path, source_identity: str,
) -> _Incumbent:
    """Check replacement provenance by bytes, not the incumbent's analytical validity."""
    if path.exists() and not path.is_file():
        raise ValueError(f"publication destination is not a file: {path}")
    if not path.exists():
        return _Incumbent()

    review_bytes, content = _read_utf8(path, label="publication incumbent")
    metadata = _parse(content, label="publication incumbent").frontmatter or {}
    if (metadata.get("generated-by") != "analyse-agentic-system"
            or metadata.get("source-identity") != source_identity):
        raise ValueError("publication destination is not a generated review of the same source")
    run_id = metadata.get("analysis-run")
    if not isinstance(run_id, str) or not re.fullmatch(
        r"AAS-\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*-\d{2}", run_id
    ):
        raise ValueError("incumbent has no valid analysis run identity")
    retained = retained_overview_path(run_id)
    if metadata.get("analysis-overview") != retained.as_posix():
        raise ValueError("incumbent must identify its canonical retained overview")
    overview_path = _repo_path(repo_root, retained)
    overview_bytes, _ = _read_utf8(overview_path, label="incumbent retained overview")
    overview_hash = sha256(overview_bytes).hexdigest()
    if metadata.get("analysis-overview-sha256") != overview_hash:
        raise ValueError("incumbent retained overview hash mismatch")
    try:
        member_set = load_member_set(overview_path)
    except ValueError as exc:
        raise ValueError(f"incumbent retained set: {exc}") from exc
    overview_metadata = member_set.overview.frontmatter
    if (overview_metadata.get("run-id") != run_id
            or overview_metadata.get("type") != OVERVIEW_TYPE
            or overview_metadata.get("reviewed-boundary") != metadata.get("reviewed-revision")
            or overview_metadata.get("result-disposition") != "complete"):
        raise ValueError("incumbent retained overview identity mismatch")
    return _Incumbent(
        review_bytes,
        {document.name: document.path for document in member_set.documents},
        {document.name: document.content for document in member_set.documents},
    )


def inspect_destination(
    *, repo_root: Path, generated_destination: str, source_identity: str,
) -> dict[str, object]:
    """Return only a replacement decision and byte identity, never prior prose."""
    repo_root = repo_root.resolve()
    path = _destination_path(repo_root, generated_destination)
    require_publishable_worktree(repo_root)
    incumbent = _check_incumbent(path=path, repo_root=repo_root, source_identity=source_identity)
    return {
        "replaceable": True,
        "exists": incumbent.review_bytes is not None,
        "expected_incumbent_sha256": incumbent.digest,
    }


def _render_final_state(
    *,
    state: AgenticAnalysisRunState,
    document: ParsedDocument,
    overview_bytes: bytes,
    generated_bytes: bytes,
    generated_destination: str,
) -> str:
    frontmatter = dict(document.frontmatter or {})
    overview_path = state.run_dir / OVERVIEW_NAME
    frontmatter.update(
        {
            "run-status": "complete",
            "result-disposition": "complete",
            "overview": {
                "path": overview_path.relative_to(state.repo_root).as_posix(),
                "sha256": sha256(overview_bytes).hexdigest(),
            },
            "generated-review": {
                "path": generated_destination,
                "sha256": sha256(generated_bytes).hexdigest(),
            },
            "failure": None,
        }
    )
    body = re.sub(
        r"(?ms)^## Outcome\s*$.*\Z",
        "## Outcome\n\nPublication completed for the exact member set and declared review projection.\n",
        document.body.rstrip() + "\n",
    )
    serialized = yaml.safe_dump(
        frontmatter,
        sort_keys=False,
        allow_unicode=True,
        width=1000,
    )
    return f"---\n{serialized}---\n{body.lstrip()}"


def _check_set(spec: PublicationSpec) -> _CheckedSet:
    repo_root = spec.repo_root.resolve()
    state_path = _repo_path(repo_root, spec.run_state_path)
    generated_candidate = _repo_path(repo_root, spec.generated_candidate_path)
    generated_path = _destination_path(
        repo_root, spec.generated_destination
    )
    running_state, state_document = _load_running_state(
        state_path, repo_root=repo_root
    )
    _require_candidate_in_run(generated_candidate, running_state)
    require_publishable_worktree(repo_root)
    try:
        member_set = load_member_set(running_state.run_dir / OVERVIEW_NAME)
    except ValueError as exc:
        raise ValueError(f"exact member set: {exc}") from exc
    if member_set.overview.frontmatter.get("result-disposition") != "complete":
        raise ValueError("publication requires a complete exact overview")
    inputs_commit = member_set.overview.frontmatter.get("inputs-commit")
    require_method_unchanged(repo_root, inputs_commit)
    require_running_package_unchanged(inputs_commit)
    incumbent = _check_incumbent(
        path=generated_path, repo_root=repo_root,
        source_identity=running_state.source.identity,
    )
    if incumbent.digest != spec.expected_incumbent_sha256:
        raise ValueError("publication destination changed since inspection")
    memory = member_set.memory
    if memory is None or "memory-comparison" not in memory.frontmatter:
        raise ValueError("publication requires memory-comparison in the memory member")
    retained_paths = {
        name: _repo_path(repo_root, path)
        for name, path in retained_set_paths(running_state.run_id).items()
    }
    for name, retained in retained_paths.items():
        if retained.relative_to(repo_root) != retained_set_paths(running_state.run_id)[name]:
            raise ValueError("retained set must use its canonical paths")
    retained_dir = retained_paths[OVERVIEW_NAME].parent
    if retained_dir.exists():
        raise ValueError(f"retained set already exists; use a new run ID: {retained_dir}")

    generated_bytes, generated_text = _read_utf8(
        generated_candidate, label="generated candidate"
    )
    final_state_text = _render_final_state(
        state=running_state,
        document=state_document,
        overview_bytes=member_set.overview.content,
        generated_bytes=generated_bytes,
        generated_destination=spec.generated_destination,
    )
    overrides = {generated_path: generated_text}
    overrides.update(
        {retained_paths[document.name]: document.text for document in member_set.documents}
    )
    results = validation.validate_note_text_at_path(
        final_state_text, path=state_path, repo_root=repo_root,
        content_overrides=overrides,
    )
    diagnostics = [*results.warns, *results.fails]
    if diagnostics:
        raise ValueError("publication set verification failed: " + "; ".join(diagnostics))

    return _CheckedSet(
        spec=PublicationSpec(
            repo_root=repo_root,
            run_state_path=state_path,
            generated_candidate_path=generated_candidate,
            generated_destination=spec.generated_destination,
            expected_incumbent_sha256=spec.expected_incumbent_sha256,
        ),
        final_state_text=final_state_text,
        generated_bytes=generated_bytes,
        member_set=member_set,
        retained_paths=retained_paths,
        incumbent=incumbent,
    )


def prepare_publication(spec: PublicationSpec) -> PreparedPublication:
    """Validate the exact member set, specialist handoff, and compact publication bytes."""
    _check_set(spec)
    return PreparedPublication()


def _atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary_path = Path(temporary)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_path, path)
    except Exception:
        temporary_path.unlink(missing_ok=True)
        raise


def _restore(path: Path, content: bytes | None) -> None:
    if content is None:
        path.unlink(missing_ok=True)
    else:
        _atomic_write(path, content)


def publish_publication(spec: PublicationSpec) -> PublishedPublication:
    """Publish a verified set, rolling back ordinary failures."""
    checked = _check_set(spec)
    repo_root = checked.spec.repo_root
    generated_path = repo_root / checked.spec.generated_destination
    state_path = checked.spec.run_state_path
    targets: list[tuple[Path, bytes]] = [
        *(
            (checked.retained_paths[document.name], document.content)
            for document in checked.member_set.documents
        ),
        (generated_path, checked.generated_bytes),
        (state_path, checked.final_state_text.encode("utf-8")),
    ]
    if checked.incumbent.review_bytes is not None:
        backups = [
            (state_path.parent / INCUMBENT_REVIEW_NAME, checked.incumbent.review_bytes),
            *(
                (state_path.parent / incumbent_copy_name(name), content)
                for name, content in checked.incumbent.set_bytes.items()
            ),
        ]
        for path, content in backups:
            if path.exists() and path.read_bytes() != content:
                raise ValueError("incumbent recovery copy already contains different bytes")
        targets = backups + targets
    old_bytes = {
        path: path.read_bytes() if path.exists() else None for path, _ in targets
    }
    if old_bytes[generated_path] != checked.incumbent.review_bytes:
        raise ValueError("publication destination changed during validation")
    for name, path in checked.incumbent.set_paths.items():
        if path.read_bytes() != checked.incumbent.set_bytes[name]:
            raise ValueError("incumbent retained set changed during validation")
    # _check_set refused an existing retained directory, so any directory
    # found here on rollback was created by this publication.
    retained_dir = checked.retained_paths[OVERVIEW_NAME].parent
    written: list[Path] = []
    try:
        for path, content in targets:
            if path == generated_path:
                current = path.read_bytes() if path.exists() else None
                if current != checked.incumbent.review_bytes:
                    raise ValueError("publication destination changed before replacement")
            _atomic_write(path, content)
            written.append(path)
        results = validation.validate_note(state_path, repo_root=repo_root)
        diagnostics = [*results.warns, *results.fails]
        if diagnostics:
            raise ValueError(
                "published run-state validation failed: " + "; ".join(diagnostics)
            )
    except Exception as publication_error:
        rollback_errors: list[str] = []
        for path in reversed(written):
            try:
                _restore(path, old_bytes[path])
            except OSError as exc:
                rollback_errors.append(f"{path}: {exc}")
        if retained_dir.exists():
            try:
                shutil.rmtree(retained_dir)
            except OSError as exc:
                rollback_errors.append(f"{retained_dir}: {exc}")
        if rollback_errors:
            raise PublicationUncertainError(
                f"publication failed ({publication_error}); rollback also failed: "
                + "; ".join(rollback_errors)
            ) from publication_error
        raise

    cleanup_warnings: list[str] = []
    candidate = checked.spec.generated_candidate_path
    try:
        candidate.unlink(missing_ok=True)
    except OSError as exc:
        cleanup_warnings.append(f"could not remove candidate {candidate}: {exc}")
    return PublishedPublication(
        generated_path=checked.spec.generated_destination,
        retained_path=checked.retained_paths[OVERVIEW_NAME].relative_to(repo_root).as_posix(),
        cleanup_warnings=tuple(cleanup_warnings),
    )

