"""Deterministic checks for workshop and task lifecycle contradictions."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

_WORKSHOP_LINK_RE = re.compile(r"\]\(\./([^/)]+)(?:/[^)]*)?\)")
_TASK_BOX_RE = re.compile(r"^\s*-\s*\[([ xX])\]", re.MULTILINE)
_CODE_PATH_RE = re.compile(r"`(kb/[^`]+)`")
_HEADING_RE_TEMPLATE = r"^##\s+{heading}\s*$"
_FRAMING_FILES = ("README.md", "framing.md", "plan.md")


@dataclass(frozen=True)
class LifecycleDiagnostic:
    diagnostic_id: str
    severity: str
    subject: Path
    reason: str


@dataclass(frozen=True)
class LifecycleValidationResults:
    subjects_inspected: int
    diagnostics: tuple[LifecycleDiagnostic, ...]


def _section(content: str, heading: str) -> str | None:
    match = re.search(
        _HEADING_RE_TEMPLATE.format(heading=re.escape(heading)),
        content,
        flags=re.MULTILINE | re.IGNORECASE,
    )
    if match is None:
        return None
    start = match.end()
    next_heading = re.search(r"^##\s+", content[start:], flags=re.MULTILINE)
    end = start + next_heading.start() if next_heading else len(content)
    return content[start:end]


def _registered_workshop_names(index: Path) -> set[str]:
    if not index.is_file():
        return set()
    return set(_WORKSHOP_LINK_RE.findall(index.read_text(encoding="utf-8")))


def _validate_workshops(repo_root: Path) -> tuple[int, list[LifecycleDiagnostic]]:
    work_root = repo_root / "kb" / "work"
    if not work_root.is_dir():
        return 0, []

    registered = _registered_workshop_names(work_root / "README.md")
    directories = sorted(
        path
        for path in work_root.iterdir()
        if (
            path.is_dir()
            and not path.name.startswith(".")
            and any(candidate.is_file() for candidate in path.rglob("*"))
        )
    )
    diagnostics: list[LifecycleDiagnostic] = []
    for directory in directories:
        if directory.name not in registered:
            diagnostics.append(
                LifecycleDiagnostic(
                    diagnostic_id="lifecycle.workshop.unregistered",
                    severity="warning",
                    subject=directory,
                    reason=(
                        "top-level workshop directory is absent from "
                        "kb/work/README.md; register active work, identify a "
                        "workflow namespace, or close completed work"
                    ),
                )
            )
        if not any((directory / name).is_file() for name in _FRAMING_FILES):
            diagnostics.append(
                LifecycleDiagnostic(
                    diagnostic_id="lifecycle.workshop.missing-framing",
                    severity="failure",
                    subject=directory,
                    reason=(
                        "top-level workshop has no README.md, framing.md, or plan.md"
                    ),
                )
            )
    return len(directories), diagnostics


def _validate_backlog_tasks(repo_root: Path) -> tuple[int, list[LifecycleDiagnostic]]:
    backlog_root = repo_root / "kb" / "tasks" / "backlog"
    if not backlog_root.is_dir():
        return 0, []

    paths = sorted(backlog_root.glob("*.md"))
    diagnostics: list[LifecycleDiagnostic] = []
    for path in paths:
        content = path.read_text(encoding="utf-8")
        tasks = _section(content, "Tasks")
        if tasks is None:
            continue
        boxes = _TASK_BOX_RE.findall(tasks)
        if boxes and all(value.lower() == "x" for value in boxes):
            diagnostics.append(
                LifecycleDiagnostic(
                    diagnostic_id="lifecycle.task.backlog-complete",
                    severity="warning",
                    subject=path,
                    reason=(
                        "backlog task has a Tasks section whose checkboxes are all "
                        "complete; move, close, or reframe it"
                    ),
                )
            )
    return len(paths), diagnostics


def _declared_output_paths(content: str) -> tuple[str, ...]:
    output = _section(content, "Output")
    if output is None:
        return ()
    return tuple(
        value
        for value in _CODE_PATH_RE.findall(output)
        if not any(character in value for character in "*?[]")
    )


def _validate_recurring_tasks(repo_root: Path) -> tuple[int, list[LifecycleDiagnostic]]:
    recurring_root = repo_root / "kb" / "tasks" / "recurring"
    if not recurring_root.is_dir():
        return 0, []

    paths = sorted(recurring_root.glob("*.md"))
    diagnostics: list[LifecycleDiagnostic] = []
    for path in paths:
        content = path.read_text(encoding="utf-8")
        for declared_path in _declared_output_paths(content):
            target = (repo_root / declared_path).resolve()
            try:
                target.relative_to(repo_root)
            except ValueError:
                continue
            if target.exists():
                continue
            diagnostics.append(
                LifecycleDiagnostic(
                    diagnostic_id="lifecycle.task.recurring-output-missing",
                    severity="warning",
                    subject=path,
                    reason=(
                        f"declared recurring output does not exist: {declared_path}; "
                        "create it on the first run or revise the destination"
                    ),
                )
            )
    return len(paths), diagnostics


def validate_lifecycle(*, repo_root: Path) -> LifecycleValidationResults:
    """Inspect bounded workshop and task lifecycle invariants."""

    resolved_root = repo_root.resolve()
    subjects_inspected = 0
    diagnostics: list[LifecycleDiagnostic] = []
    for validator in (
        _validate_workshops,
        _validate_backlog_tasks,
        _validate_recurring_tasks,
    ):
        count, findings = validator(resolved_root)
        subjects_inspected += count
        diagnostics.extend(findings)
    return LifecycleValidationResults(
        subjects_inspected=subjects_inspected,
        diagnostics=tuple(diagnostics),
    )
