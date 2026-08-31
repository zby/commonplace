"""Read-only project situation projection for agent and operator use."""

from __future__ import annotations

import sqlite3
import subprocess
import tomllib
from dataclasses import dataclass
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

from commonplace.freshness.status import load_target_status
from commonplace.lib.lifecycle_validation import validate_lifecycle
from commonplace.lib.project_paths import (
    kb_root,
    list_collection_validation_paths,
)
from commonplace.lib.validation import run_validation
from commonplace.review.review_db import connect
from commonplace.review.warn_selector import scan_reviews
from commonplace.store import resolve_db_path


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


@dataclass(frozen=True)
class ReviewStatus:
    available: bool
    actionable_warn_notes: int = 0
    actionable_warn_findings: int = 0
    stale_warn_pairs: int = 0
    queued_jobs: int = 0
    queued_pairs: int = 0
    failed_jobs: int = 0
    failed_pairs: int = 0
    stale_freshness_targets: int = 0
    missing_input_targets: int = 0
    version_error_targets: int = 0
    error: str | None = None


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


def load_notes_validation_status(repo_root: Path) -> CheckStatus:
    collection = (kb_root(repo_root) / "notes").resolve()
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
        details_command="commonplace-validate notes",
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
    )


def _job_counts(conn: sqlite3.Connection) -> dict[str, tuple[int, int]]:
    rows = conn.execute(
        """
        SELECT
            j.status,
            count(DISTINCT j.review_job_id) AS job_count,
            count(rp.review_pair_id) AS pair_count
        FROM review_jobs AS j
        LEFT JOIN review_pairs AS rp
          ON rp.review_job_id = j.review_job_id
        WHERE j.status IN ('queued', 'failed')
        GROUP BY j.status
        """
    ).fetchall()
    return {
        str(row["status"]): (int(row["job_count"]), int(row["pair_count"]))
        for row in rows
    }


def load_review_status(repo_root: Path, *, db_override: str | None = None) -> ReviewStatus:
    db_path = resolve_db_path(repo_root, db_override)
    if not db_path.is_file():
        return ReviewStatus(available=False, error=f"store not found: {db_path}")
    try:
        notes, stale_warn_pairs = scan_reviews(repo_root, db_path=db_path)
        with connect(db_path) as conn:
            jobs = _job_counts(conn)
            freshness = load_target_status(
                conn,
                repo_root=repo_root,
                include_fresh=False,
                include_diff=False,
            )
    except (OSError, RuntimeError, ValueError, sqlite3.Error) as exc:
        return ReviewStatus(available=False, error=str(exc))

    queued_jobs, queued_pairs = jobs.get("queued", (0, 0))
    failed_jobs, failed_pairs = jobs.get("failed", (0, 0))
    missing_input_targets = sum(
        any(item.status == "input-missing" for item in target.changed_inputs)
        for target in freshness.targets
    )
    version_error_targets = sum(
        any(item.status == "version-error" for item in target.changed_inputs)
        for target in freshness.targets
    )
    return ReviewStatus(
        available=True,
        actionable_warn_notes=len(notes),
        actionable_warn_findings=sum(note.count for note in notes),
        stale_warn_pairs=len(stale_warn_pairs),
        queued_jobs=queued_jobs,
        queued_pairs=queued_pairs,
        failed_jobs=failed_jobs,
        failed_pairs=failed_pairs,
        stale_freshness_targets=len(freshness.targets),
        missing_input_targets=missing_input_targets,
        version_error_targets=version_error_targets,
    )


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
                "status.review.inspect-store",
                "failure",
                review.error,
                "commonplace-freshness-status",
            )
        )
    if review.actionable_warn_findings:
        actions.append(
            StatusAction(
                "status.review.triage-warnings",
                "warning",
                (
                    f"{review.actionable_warn_findings} current actionable review "
                    f"findings affect {review.actionable_warn_notes} notes"
                ),
                "commonplace-warn-selector",
            )
        )
    if review.failed_jobs:
        actions.append(
            StatusAction(
                "status.review.inspect-failed-jobs",
                "warning",
                f"{review.failed_jobs} failed review jobs contain {review.failed_pairs} pairs",
                "commonplace-review-job-list --status failed",
            )
        )
    if review.missing_input_targets:
        actions.append(
            StatusAction(
                "status.freshness.retire-missing-inputs",
                "warning",
                (
                    f"{review.missing_input_targets} stale targets reference deleted "
                    "inputs and need retirement review"
                ),
                "commonplace-freshness-status --missing",
            )
        )
    if review.version_error_targets:
        actions.append(
            StatusAction(
                "status.freshness.inspect-version-errors",
                "failure",
                f"{review.version_error_targets} freshness targets have version errors",
                "commonplace-freshness-status",
            )
        )
    if review.queued_jobs:
        actions.append(
            StatusAction(
                "status.review.resume-queued-jobs",
                "warning",
                f"{review.queued_jobs} queued review jobs contain {review.queued_pairs} pairs",
                "commonplace-review-job-list --status queued",
            )
        )
    if review.stale_freshness_targets:
        actions.append(
            StatusAction(
                "status.freshness.inspect-stale-targets",
                "warning",
                f"{review.stale_freshness_targets} registered targets are stale",
                "commonplace-freshness-status",
            )
        )
    return tuple(actions)


def load_project_status(
    *,
    repo_root: Path,
    db_override: str | None = None,
    include_review: bool = False,
) -> ProjectStatus:
    resolved_root = repo_root.resolve()
    project_version = _project_version(resolved_root)
    command_version = _command_version()
    notes_validation = load_notes_validation_status(resolved_root)
    lifecycle = load_lifecycle_status(resolved_root)
    review = (
        load_review_status(resolved_root, db_override=db_override)
        if include_review
        else None
    )
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
