"""Prepare and publish one exact agentic-analysis set at its stable source path."""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass, field
from hashlib import sha256
from pathlib import Path

import yaml

from commonplace.lib import validation
from commonplace.lib.agentic_analysis import AgenticAnalysisRunState, load_run_state
from commonplace.lib.agentic_set import (
    ARCHIVE_ROOT,
    MANIFEST_NAME,
    OUTPUT_DIR,
    OVERVIEW_NAME,
    RETAINED_ROOT,
    SET_NAMES,
    MemberSet,
    current_analyses,
    is_review_path,
    load_member_set,
    normalize_source_identity,
    source_slug,
)
from commonplace.lib.note_parser import ParsedDocument, parse_document

# The files whose tree at ``inputs-commit`` supplied the run's method. A run
# publishes only while HEAD leaves them unchanged since that commit.
METHOD_PATHS: tuple[str, ...] = (
    "src/commonplace/",
    "kb/agentic-system-analyses/COLLECTION.md",
    "kb/agentic-system-analyses/instructions/publish-analysis.md",
    "kb/agentic-system-analyses/instructions/analyse-agentic-system/",
    "kb/agentic-system-analyses/instructions/agentic-analysis-boundary.md",
    "kb/agentic-system-analyses/instructions/agentic-analysis-sources.md",
    "kb/agentic-system-analyses/instructions/agentic-analysis-records.md",
    "kb/agentic-system-analyses/types/agentic-system-analysis-set.md",
    "kb/agentic-system-analyses/types/agentic-system-analysis-set.schema.yaml",
    "kb/agentic-system-analyses/types/agentic-system-analysis-overview.md",
    "kb/agentic-system-analyses/types/agentic-system-analysis-overview.schema.yaml",
    "kb/agentic-system-analyses/types/agentic-system-reconciliation-report.md",
    "kb/agentic-system-analyses/types/agentic-system-reconciliation-report.schema.yaml",
    "kb/agentic-system-analyses/types/agentic-system-runtime-report.md",
    "kb/agentic-system-analyses/types/agentic-system-runtime-report.schema.yaml",
    "kb/agentic-system-analyses/types/agentic-system-epistemic-report.md",
    "kb/agentic-system-analyses/types/agentic-system-epistemic-report.schema.yaml",
    "kb/agentic-system-analyses/types/agent-memory-analysis-report.md",
    "kb/agentic-system-analyses/types/agent-memory-analysis-report.schema.yaml",
    "kb/agentic-system-analyses/types/agentic-system-analysis-run-state.md",
    "kb/agentic-system-analyses/types/agentic-system-analysis-run-state.schema.yaml",
    # Every member schema references these.
    "kb/types/note.schema.yaml",
    "kb/types/note-base.schema.yaml",
)

# Untracked or modified files may sit here while a batch runs: a sibling run's
# publication that has not been committed yet.
OUTPUT_LOCATIONS: tuple[str, ...] = (f"{RETAINED_ROOT.as_posix()}/", f"{ARCHIVE_ROOT.as_posix()}/")


@dataclass(frozen=True)
class PublicationSpec:
    repo_root: Path
    run_state_path: Path
    generated_candidate_path: Path
    generated_destination: str
    expected_incumbent_sha256: str


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
    if not is_review_path(raw):
        raise ValueError(
            "publication destination must be kb/agentic-system-analyses/retained/<slug>/overview.md: "
            f"{raw}"
        )
    path = repo_root / raw
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
    state = load_run_state(path, repo_root=repo_root)
    if state.status != "running":
        raise ValueError("publication requires a running run state")
    if state.source is None:
        raise ValueError("publication requires a frozen source in the run state")
    _, content = _read_utf8(path, label="run state")
    return state, _parse(content, label="run state")


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
    """Validate every current set before choosing a replacement."""
    source_identity = normalize_source_identity(source_identity)
    sets = current_analyses(repo_root)
    for member_set in sets:
        if member_set.overview.path != path:
            continue
        if member_set.memory.frontmatter["source-identity"] != source_identity:
            raise ValueError("publication destination belongs to another source")
        return _Incumbent(
            member_set.overview.content,
            {MANIFEST_NAME: member_set.artifact.path / MANIFEST_NAME,
             **{document.name: document.path for document in member_set.documents}},
            {MANIFEST_NAME: member_set.artifact.content,
             **{document.name: document.content for document in member_set.documents}},
        )
    return _Incumbent()


def inspect_destination(
    *, repo_root: Path, generated_destination: str, source_identity: str,
) -> dict[str, object]:
    """Return only a replacement decision and byte identity, never prior prose."""
    repo_root = repo_root.resolve()
    path = _destination_path(repo_root, generated_destination)
    require_publishable_worktree(repo_root)
    incumbent = _check_incumbent(path=path, repo_root=repo_root, source_identity=source_identity)
    return {
        "exists": incumbent.review_bytes is not None,
        "expected_incumbent_sha256": incumbent.digest,
    }


def _render_final_state(
    *,
    state: AgenticAnalysisRunState,
    document: ParsedDocument,
    artifact_bytes: bytes,
    generated_bytes: bytes,
    generated_destination: str,
) -> str:
    frontmatter = dict(document.frontmatter or {})
    artifact_path = state.run_dir / OUTPUT_DIR / MANIFEST_NAME
    frontmatter.update(
        {
            "run-status": "complete",
            "result-disposition": "complete",
            "artifact": {
                "path": artifact_path.relative_to(state.repo_root).as_posix(),
                "sha256": sha256(artifact_bytes).hexdigest(),
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
        "## Outcome\n\nPublication completed for the exact member set and its accepted overview.\n",
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
    if generated_candidate != running_state.run_dir / OUTPUT_DIR / OVERVIEW_NAME:
        raise ValueError("publication candidate must be the accepted output/overview.md")
    require_publishable_worktree(repo_root)
    run = validation.ValidationRun(repo_root, ())
    try:
        member_set = load_member_set(running_state.run_dir / OUTPUT_DIR, run=run)
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
    retained_dir = generated_path.parent
    if retained_dir.resolve() != retained_dir:
        raise ValueError("retained set must use its canonical paths")
    expected_path = RETAINED_ROOT / source_slug(running_state.source.identity, running_state.system) / OVERVIEW_NAME
    if generated_path.relative_to(repo_root) != expected_path:
        raise ValueError("publication directory name does not match its source")
    if incumbent.review_bytes is not None:
        incumbent_meta = _parse(incumbent.review_bytes.decode("utf-8"), label="incumbent").frontmatter
        if incumbent_meta["run-id"] == running_state.run_id:
            raise ValueError("replacement requires a new run ID")
        archive = repo_root / ARCHIVE_ROOT / incumbent_meta["run-id"]
        if archive.exists():
            raise ValueError(f"archive destination already exists: {archive}")
    retained_paths = {name: retained_dir / name for name in (MANIFEST_NAME, *SET_NAMES)}

    generated_bytes, _ = _read_utf8(
        generated_candidate, label="generated candidate"
    )
    final_state_text = _render_final_state(
        state=running_state,
        document=state_document,
        artifact_bytes=member_set.artifact.content,
        generated_bytes=generated_bytes,
        generated_destination=spec.generated_destination,
    )
    if generated_bytes != member_set.overview.content:
        raise ValueError("publication overview changed during validation")
    overrides = {generated_path: generated_bytes, retained_paths[MANIFEST_NAME]: member_set.artifact.content}
    overrides.update(
        {retained_paths[document.name]: document.content for document in member_set.documents}
    )
    # Validate the completed state against the future retained bytes in a
    # fresh context, including when an incumbent occupies those paths.
    overrides[state_path] = final_state_text
    run = validation.ValidationRun(repo_root, (), content_overrides=overrides)
    results = run.validate(state_path)
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


def prepare_publication(spec: PublicationSpec) -> None:
    """Validate the exact member set and its public overview."""
    _check_set(spec)


def atomic_write(path: Path, content: bytes) -> None:
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


def publish_publication(spec: PublicationSpec) -> PublishedPublication:
    """Validate before replacing, archive unchanged bytes, and restore on errors."""
    checked = _check_set(spec)
    repo_root = checked.spec.repo_root
    state_path = checked.spec.run_state_path
    retained_dir = checked.retained_paths[OVERVIEW_NAME].parent
    archive = None
    old_state = state_path.read_bytes()
    moved = False
    created = False
    # Recheck exact incumbent bytes after validation and before any mutation.
    for name, path in checked.incumbent.set_paths.items():
        if path.read_bytes() != checked.incumbent.set_bytes[name]:
            raise ValueError("incumbent retained set changed during validation")
    if checked.incumbent.review_bytes is not None:
        metadata = _parse(checked.incumbent.review_bytes.decode("utf-8"), label="incumbent").frontmatter
        archive = repo_root / ARCHIVE_ROOT / metadata["run-id"]
    elif retained_dir.exists():
        raise ValueError("publication destination appeared during validation")
    try:
        if archive is not None:
            archive.parent.mkdir(parents=True, exist_ok=True)
            retained_dir.rename(archive)
            moved = True
        retained_dir.mkdir(parents=True, exist_ok=False)
        created = True
        for name, content in {
            MANIFEST_NAME: checked.member_set.artifact.content,
            **{document.name: document.content for document in checked.member_set.documents},
        }.items():
            atomic_write(retained_dir / name, content)
        atomic_write(state_path, checked.final_state_text.encode("utf-8"))
    except Exception as publication_error:
        try:
            if created:
                shutil.rmtree(retained_dir)
            if moved:
                archive.rename(retained_dir)
            if state_path.read_bytes() != old_state:
                atomic_write(state_path, old_state)
        except OSError as rollback_error:
            raise PublicationUncertainError(
                f"publication failed ({publication_error}); rollback also failed: {rollback_error}"
            ) from publication_error
        raise
    return PublishedPublication(
        generated_path=checked.spec.generated_destination,
        retained_path=checked.retained_paths[MANIFEST_NAME].relative_to(repo_root).as_posix(),
        cleanup_warnings=(),
    )
