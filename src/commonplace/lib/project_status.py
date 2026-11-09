"""Read-only project situation projection for agent and operator use."""

from __future__ import annotations

import shlex
import subprocess
import tomllib
from dataclasses import dataclass
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

from commonplace.lib.lifecycle_validation import validate_lifecycle
from commonplace.lib.project_paths import (
    list_collection_validation_paths,
    resolve_collection,
)
from commonplace.lib.review_workflows import results
from commonplace.lib.validation import run_validation


@dataclass(frozen=True)
class StatusAction:
    action_id: str
    severity: str
    reason: str
    command: str


@dataclass(frozen=True)
class GitStatus:
    available: bool
    head: str | None
    changed_paths: int | None
    error: str | None = None


@dataclass(frozen=True)
class CheckStatus:
    status: str
    subjects: int
    failures: int
    warnings: int
    details_command: str
    scope: str


@dataclass(frozen=True)
class ReviewStatus:
    """Counts over the stored review results; `warn` and `fail` count fresh results only."""

    results: int = 0
    fresh: int = 0
    stale: int = 0
    orphaned: int = 0
    warn: int = 0
    fail: int = 0
    error: str | None = None          # a result file that could not be read


@dataclass(frozen=True)
class ProjectStatus:
    repo_root: str
    project_version: str | None
    command_version: str | None
    git: GitStatus
    notes_validation: CheckStatus
    lifecycle: CheckStatus
    review: ReviewStatus | None
    actions: tuple[StatusAction, ...]

    @property
    def status(self) -> str:
        if (
            self.notes_validation.status == "failed"
            or self.lifecycle.status == "failed"
            or (self.review is not None and self.review.error is not None)
            or any(action.severity == "failure" for action in self.actions)
        ):
            return "failed"
        if self.actions:
            return "warning"
        return "success"


def _run_git(repo_root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_root,
        check=False,
        capture_output=True,
        text=True,
        timeout=10,
    )


def load_git_status(repo_root: Path) -> GitStatus:
    try:
        head_result = _run_git(repo_root, "rev-parse", "HEAD")
        status_result = _run_git(repo_root, "status", "--porcelain=v1")
    except (OSError, subprocess.SubprocessError) as exc:
        return GitStatus(False, None, None, str(exc))
    if head_result.returncode or status_result.returncode:
        error = (head_result.stderr or status_result.stderr).strip()
        return GitStatus(False, None, None, error or "not a Git worktree")
    changed_paths = sum(bool(line) for line in status_result.stdout.splitlines())
    return GitStatus(True, head_result.stdout.strip(), changed_paths)


def _project_version(repo_root: Path) -> str | None:
    pyproject = repo_root / "pyproject.toml"
    if not pyproject.is_file():
        return None
    try:
        payload = tomllib.loads(pyproject.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError):
        return None
    value = payload.get("project", {}).get("version")
    return value if isinstance(value, str) else None


def _command_version() -> str | None:
    try:
        return version("llm-commonplace")
    except PackageNotFoundError:
        return None


def load_notes_validation_status(repo_root: Path, collection: str) -> CheckStatus:
    collection = resolve_collection(collection, repo_root)
    paths = tuple(list_collection_validation_paths(collection))
    outcome = run_validation(
        paths,
        repo_root=repo_root,
        collection=collection,
    )
    failures = sum(len(outcome.results[path].fails) for path in outcome.paths)
    failures += len(outcome.collection_structure)
    warnings = sum(len(outcome.results[path].warns) for path in outcome.paths)
    warnings += len(outcome.collection_warnings)
    status = "failed" if failures else "warning" if warnings else "success"
    return CheckStatus(
        status=status,
        subjects=len(outcome.paths),
        failures=failures,
        warnings=warnings,
        details_command=shlex.join([
            "commonplace-validate", collection.relative_to(repo_root).as_posix(),
        ]),
        scope=collection.relative_to(repo_root).as_posix(),
    )


def load_lifecycle_status(repo_root: Path) -> CheckStatus:
    results = validate_lifecycle(repo_root=repo_root)
    failures = sum(item.severity == "failure" for item in results.diagnostics)
    warnings = sum(item.severity == "warning" for item in results.diagnostics)
    status = "failed" if failures else "warning" if warnings else "success"
    return CheckStatus(
        status=status,
        subjects=results.subjects_inspected,
        failures=failures,
        warnings=warnings,
        details_command="commonplace-validate lifecycle",
        scope="kb/work and kb/tasks",
    )


def load_review_status(repo_root: Path) -> ReviewStatus:
    try:
        summary = results.summarize(repo_root)
    except (OSError, ValueError) as exc:
        return ReviewStatus(error=str(exc))
    return ReviewStatus(results=summary.results, fresh=summary.fresh, stale=summary.stale,
                        orphaned=summary.orphaned, warn=summary.warn, fail=summary.fail)


def _actions(
    project_version: str | None,
    command_version: str | None,
    notes_validation: CheckStatus,
    lifecycle: CheckStatus,
    review: ReviewStatus | None,
) -> tuple[StatusAction, ...]:
    actions: list[StatusAction] = []
    if (
        project_version is not None
        and command_version is not None
        and project_version != command_version
    ):
        actions.append(
            StatusAction(
                "status.version.inspect-skew",
                "failure",
                (
                    f"project version {project_version} differs from active command "
                    f"version {command_version}"
                ),
                "commonplace-source",
            )
        )
    if notes_validation.failures or notes_validation.warnings:
        actions.append(
            StatusAction(
                "status.validation.inspect",
                "failure" if notes_validation.failures else "warning",
                (
                    f"notes validation has {notes_validation.failures} failures and "
                    f"{notes_validation.warnings} warnings"
                ),
                notes_validation.details_command,
            )
        )
    if lifecycle.failures or lifecycle.warnings:
        actions.append(
            StatusAction(
                "status.lifecycle.reconcile",
                "failure" if lifecycle.failures else "warning",
                (
                    f"lifecycle validation has {lifecycle.failures} failures and "
                    f"{lifecycle.warnings} warnings"
                ),
                lifecycle.details_command,
            )
        )
    if review is None:
        return tuple(actions)
    if review.error is not None:
        actions.append(
            StatusAction(
                "status.review.inspect-results",
                "failure",
                review.error,
                "commonplace-review status",
            )
        )
    if review.fail:
        actions.append(
            StatusAction(
                "status.review.fix-failures",
                "warning",
                f"{review.fail} current review results fail",
                "commonplace-review status --fresh --outcome fail",
            )
        )
    if review.warn:
        actions.append(
            StatusAction(
                "status.review.triage-warnings",
                "warning",
                f"{review.warn} current review results warn",
                "commonplace-review status --fresh --outcome warn",
            )
        )
    if review.stale:
        actions.append(
            StatusAction(
                "status.review.rerun-stale",
                "warning",
                f"{review.stale} review results are stale; rerun their pairs with commonplace-review run gates",
                "commonplace-review status --stale",
            )
        )
    if review.orphaned:
        actions.append(
            StatusAction(
                "status.review.delete-orphans",
                "warning",
                f"{review.orphaned} review results name a deleted note or criterion; delete their files",
                "commonplace-review status",
            )
        )
    return tuple(actions)


def load_project_status(
    *,
    repo_root: Path,
    collection: str,
    include_review: bool = False,
) -> ProjectStatus:
    resolved_root = repo_root.resolve()
    project_version = _project_version(resolved_root)
    command_version = _command_version()
    notes_validation = load_notes_validation_status(resolved_root, collection)
    lifecycle = load_lifecycle_status(resolved_root)
    review = load_review_status(resolved_root) if include_review else None
    return ProjectStatus(
        repo_root=str(resolved_root),
        project_version=project_version,
        command_version=command_version,
        git=load_git_status(resolved_root),
        notes_validation=notes_validation,
        lifecycle=lifecycle,
        review=review,
        actions=_actions(
            project_version,
            command_version,
            notes_validation,
            lifecycle,
            review,
        ),
    )
