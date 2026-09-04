"""Deterministic validator for KB artifacts and repository invariants."""

from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import sys
import tempfile
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

from commonplace.lib.lifecycle_validation import validate_lifecycle
from commonplace.lib.project_paths import (
    kb_root,
    list_collection_validation_paths,
    list_notes_collection_paths,
    list_type_spec_paths,
    resolve_note,
    validation_ignored_dirs,
)
from commonplace.lib.validation import (
    CheckResults,
    ValidationRunResults,
    run_validation,
    validate_collection_landings,
    validate_redirect_map,
)

_TOO_BROAD_MESSAGE = (
    "Validation scope must be a specific collection or file. "
    "Pass a collection name or path, types, landings, redirects, or a note path."
)


@dataclass(frozen=True)
class ResolvedValidationTarget:
    paths: tuple[Path, ...]
    collection: Path | None = None
    ignored_dirs: tuple[Path, ...] = ()


@dataclass(frozen=True)
class ValidationDiagnostic:
    diagnostic_id: str
    severity: str
    subject: str
    reason: str


@dataclass(frozen=True)
class AnalysedArtifact:
    path: str
    note_type: str
    warnings: int
    failures: int


@dataclass(frozen=True)
class ValidationReport:
    target: str
    scope: str
    files_analysed: int
    text_files: int
    warning_subjects: int
    failing_subjects: int
    diagnostics: tuple[ValidationDiagnostic, ...]
    analysed_artifacts: tuple[AnalysedArtifact, ...] = ()
    excluded_subtrees: tuple[str, ...] = ()

    @property
    def warning_count(self) -> int:
        return sum(item.severity == "warning" for item in self.diagnostics)

    @property
    def failure_count(self) -> int:
        return sum(item.severity == "failure" for item in self.diagnostics)

    @property
    def status(self) -> str:
        if self.failure_count:
            return "failed"
        if self.warning_count:
            return "warning"
        return "success"


def _collection_target(collection: Path) -> ResolvedValidationTarget:
    resolved = collection.resolve()
    return ResolvedValidationTarget(
        paths=tuple(list_collection_validation_paths(resolved)),
        collection=resolved,
        ignored_dirs=tuple(validation_ignored_dirs(resolved)),
    )


def resolve_validation_target(
    arg: str, *, repo_root: Path
) -> ResolvedValidationTarget:
    if arg == "all":
        raise ValueError(_TOO_BROAD_MESSAGE)
    if arg == "notes":
        collection = (kb_root(repo_root) / "notes").resolve()
        return _collection_target(collection)
    if arg == "types":
        return ResolvedValidationTarget(paths=tuple(list_type_spec_paths(repo_root)))

    if arg in {"recent", "today"}:
        today = datetime.now(UTC).astimezone().date()
        return ResolvedValidationTarget(
            paths=tuple(
                sorted(
                    path
                    for path in list_notes_collection_paths(repo_root)
                    if datetime.fromtimestamp(path.stat().st_mtime, tz=UTC)
                    .astimezone()
                    .date()
                    == today
                )
            )
        )

    kb = kb_root(repo_root).resolve()

    candidate = Path(arg)
    if candidate.is_absolute() and candidate.is_file():
        return ResolvedValidationTarget(paths=(candidate.resolve(),))
    if candidate.is_absolute() and candidate.is_dir():
        resolved = candidate.resolve()
        if resolved == kb:
            raise ValueError(_TOO_BROAD_MESSAGE)
        return _collection_target(resolved)

    repo_candidate = (repo_root / arg).resolve()
    if repo_candidate.is_file():
        return ResolvedValidationTarget(paths=(repo_candidate,))
    if repo_candidate.is_dir():
        if repo_candidate == kb:
            raise ValueError(_TOO_BROAD_MESSAGE)
        return _collection_target(repo_candidate)

    collection_candidate = (kb_root(repo_root) / arg).resolve()
    if collection_candidate.is_dir():
        if collection_candidate == kb:
            raise ValueError(_TOO_BROAD_MESSAGE)
        return _collection_target(collection_candidate)

    return ResolvedValidationTarget(paths=(resolve_note(arg, repo_root),))


def _display_path(path: Path, *, repo_root: Path) -> str:
    try:
        return str(path.relative_to(repo_root))
    except ValueError:
        return str(path)


def format_block(path: Path, results: CheckResults) -> str:
    lines = [f"=== VALIDATION: {path.name} ===", "", f"Type: {results.note_type}", ""]

    for label, items in (
        ("PASS", results.passes),
        ("WARN", results.warns),
        ("FAIL", results.fails),
        ("INFO", results.infos),
    ):
        lines.append(f"{label}:")
        if items:
            lines.extend(f"- {item}" for item in items)
        else:
            lines.append("- (none)")
        lines.append("")

    if results.fails:
        overall = f"FAIL ({len(results.fails)} fails"
        if results.warns:
            overall += f", {len(results.warns)} warnings"
        overall += ")"
    else:
        overall = "PASS"
        if results.warns:
            overall += f" ({len(results.warns)} warnings)"
        else:
            overall += " (clean)"

    lines.append(f"Overall: {overall}")
    lines.append("===")
    return "\n".join(lines)


def _diagnostic_id(message: str, *, family: str = "artifact") -> str:
    body = message.strip()
    prefix = re.match(r"^\[([a-zA-Z0-9_-]+)\]\s*", body)
    if prefix:
        family = prefix.group(1)
        body = body[prefix.end() :]

    label, separator, _detail = body.partition(":")
    if not separator:
        label = family
    slug = re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")
    family_slug = re.sub(r"[^a-z0-9]+", "-", family.lower()).strip("-")
    if slug == family_slug:
        return f"validation.{family_slug}"
    return f"validation.{family_slug}.{slug}"


def _diagnostic(
    *,
    severity: str,
    subject: Path,
    reason: str,
    repo_root: Path,
    family: str = "artifact",
) -> ValidationDiagnostic:
    return ValidationDiagnostic(
        diagnostic_id=_diagnostic_id(reason, family=family),
        severity=severity,
        subject=_display_path(subject, repo_root=repo_root),
        reason=reason,
    )


def build_validation_report(
    *,
    target_arg: str,
    target: ResolvedValidationTarget,
    outcome: ValidationRunResults,
    repo_root: Path,
) -> ValidationReport:
    diagnostics: list[ValidationDiagnostic] = []
    warning_subjects: set[Path] = set()
    failing_subjects: set[Path] = set()
    text_files = 0

    for path in outcome.paths:
        results = outcome.results[path]
        if results.note_type == "text":
            text_files += 1
        if results.warns:
            warning_subjects.add(path)
        if results.fails:
            failing_subjects.add(path)
        diagnostics.extend(
            _diagnostic(
                severity="warning",
                subject=path,
                reason=reason,
                repo_root=repo_root,
            )
            for reason in results.warns
        )
        diagnostics.extend(
            _diagnostic(
                severity="failure",
                subject=path,
                reason=reason,
                repo_root=repo_root,
            )
            for reason in results.fails
        )
        diagnostics.extend(
            _diagnostic(
                severity="info",
                subject=path,
                reason=reason,
                repo_root=repo_root,
            )
            for reason in [
                *results.infos,
                *(item for item in results.passes if "skipped" in item.lower()),
            ]
        )

    for path, reason in outcome.collection_warnings:
        warning_subjects.add(path)
        diagnostics.append(
            _diagnostic(
                severity="warning",
                subject=path,
                reason=reason,
                repo_root=repo_root,
                family="collection-warning",
            )
        )
    for path, reason in outcome.collection_structure:
        failing_subjects.add(path)
        diagnostics.append(
            _diagnostic(
                severity="failure",
                subject=path,
                reason=reason,
                repo_root=repo_root,
                family="collection-structure",
            )
        )

    scope = (
        _display_path(target.collection, repo_root=repo_root)
        if target.collection is not None
        else target_arg
    )
    return ValidationReport(
        target=target_arg,
        scope=scope,
        files_analysed=len(outcome.paths),
        text_files=text_files,
        warning_subjects=len(warning_subjects),
        failing_subjects=len(failing_subjects),
        diagnostics=tuple(diagnostics),
        analysed_artifacts=tuple(
            AnalysedArtifact(
                path=_display_path(path, repo_root=repo_root),
                note_type=outcome.results[path].note_type,
                warnings=len(outcome.results[path].warns),
                failures=len(outcome.results[path].fails),
            )
            for path in outcome.paths
        ),
        excluded_subtrees=tuple(
            _display_path(path, repo_root=repo_root) for path in target.ignored_dirs
        ),
    )


def build_single_validation_report(
    *,
    target_arg: str,
    path: Path,
    results: CheckResults,
    repo_root: Path,
) -> ValidationReport:
    diagnostics = (
        *(
            _diagnostic(
                severity="warning",
                subject=path,
                reason=reason,
                repo_root=repo_root,
            )
            for reason in results.warns
        ),
        *(
            _diagnostic(
                severity="failure",
                subject=path,
                reason=reason,
                repo_root=repo_root,
            )
            for reason in results.fails
        ),
        *(
            _diagnostic(
                severity="info",
                subject=path,
                reason=reason,
                repo_root=repo_root,
            )
            for reason in [
                *results.infos,
                *(item for item in results.passes if "skipped" in item.lower()),
            ]
        ),
    )
    return ValidationReport(
        target=target_arg,
        scope=target_arg,
        files_analysed=1,
        text_files=int(results.note_type == "text"),
        warning_subjects=int(bool(results.warns)),
        failing_subjects=int(bool(results.fails)),
        diagnostics=diagnostics,
        analysed_artifacts=(
            AnalysedArtifact(
                path=_display_path(path, repo_root=repo_root),
                note_type=results.note_type,
                warnings=len(results.warns),
                failures=len(results.fails),
            ),
        ),
    )


def build_lifecycle_report(*, repo_root: Path) -> ValidationReport:
    results = validate_lifecycle(repo_root=repo_root)
    diagnostics = tuple(
        ValidationDiagnostic(
            diagnostic_id=item.diagnostic_id,
            severity=item.severity,
            subject=_display_path(item.subject, repo_root=repo_root),
            reason=item.reason,
        )
        for item in results.diagnostics
    )
    return ValidationReport(
        target="lifecycle",
        scope="kb/work and kb/tasks",
        files_analysed=results.subjects_inspected,
        text_files=results.subjects_inspected,
        warning_subjects=len(
            {item.subject for item in diagnostics if item.severity == "warning"}
        ),
        failing_subjects=len(
            {item.subject for item in diagnostics if item.severity == "failure"}
        ),
        diagnostics=diagnostics,
    )


def format_compact_report(report: ValidationReport) -> str:
    lines = [
        f"VALIDATION {report.status.upper()}",
        f"Target: {report.target}",
        f"Scope: {report.scope}",
        f"Files analysed: {report.files_analysed}",
        f"Text files: {report.text_files}",
        (
            "Diagnostics: "
            f"{report.failure_count} failures across {report.failing_subjects} subjects; "
            f"{report.warning_count} warnings across {report.warning_subjects} subjects"
        ),
    ]
    if report.excluded_subtrees:
        lines.append(
            "Excluded subtrees: " + ", ".join(report.excluded_subtrees)
        )

    for severity, heading in (
        ("failure", "FAILURES"),
        ("warning", "WARNINGS"),
        ("info", "NOTICES"),
    ):
        selected = [
            diagnostic
            for diagnostic in report.diagnostics
            if diagnostic.severity == severity
        ]
        if not selected:
            continue
        lines.extend(("", f"{heading}:"))
        lines.extend(
            f"- {item.diagnostic_id} | {item.subject} | {item.reason}"
            for item in selected
        )

    detail_target = shlex.quote(report.target)
    lines.extend(("", f"Details: commonplace-validate --full {detail_target}"))
    return "\n".join(lines)


def format_json_report(report: ValidationReport) -> str:
    payload = {
        "schema": "commonplace.validation.v1",
        "status": report.status,
        "target": report.target,
        "scope": report.scope,
        "summary": {
            "files_analysed": report.files_analysed,
            "text_files": report.text_files,
            "warning_subjects": report.warning_subjects,
            "failing_subjects": report.failing_subjects,
            "warnings": report.warning_count,
            "failures": report.failure_count,
        },
        "diagnostics": [
            {
                "id": item.diagnostic_id,
                "severity": item.severity,
                "subject": item.subject,
                "reason": item.reason,
            }
            for item in report.diagnostics
        ],
        "analysed_artifacts": [
            {
                "path": item.path,
                "type": item.note_type,
                "warnings": item.warnings,
                "failures": item.failures,
            }
            for item in report.analysed_artifacts
        ],
        "excluded_subtrees": list(report.excluded_subtrees),
        "details_command": f"commonplace-validate --full {shlex.quote(report.target)}",
    }
    return json.dumps(payload, indent=2, sort_keys=True)


def emit_json_report(report: ValidationReport, *, output_path: Path | None) -> None:
    """Emit one JSON receipt and optionally persist those exact bytes atomically."""
    payload = (format_json_report(report) + "\n").encode("utf-8")
    if output_path is not None:
        destination = output_path.resolve()
        if not destination.parent.is_dir():
            raise OSError(
                f"validation output parent does not exist: {destination.parent}"
            )
        file_descriptor, temporary_name = tempfile.mkstemp(
            prefix=f".{destination.name}.",
            dir=destination.parent,
        )
        temporary = Path(temporary_name)
        try:
            with os.fdopen(file_descriptor, "wb") as stream:
                stream.write(payload)
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary, destination)
        finally:
            temporary.unlink(missing_ok=True)
    sys.stdout.buffer.write(payload)


def _print_full_collection_report(
    *,
    target: ResolvedValidationTarget,
    outcome: ValidationRunResults,
    repo_root: Path,
) -> None:
    warning_items: list[tuple[Path, str]] = []
    failure_items: list[tuple[Path, str]] = []
    text_count = 0
    warning_count = 0
    failure_count = 0

    for path in outcome.paths:
        results = outcome.results[path]
        if results.note_type == "text":
            text_count += 1
        print(format_block(path, results))
        if results.warns:
            warning_count += 1
            warning_items.extend((path, warning) for warning in results.warns)
        if results.fails:
            failure_count += 1
            failure_items.extend((path, failure) for failure in results.fails)

    if target.collection is None:
        return

    warning_items.extend(outcome.collection_warnings)
    print("\n=== BATCH INFO ===\n")
    print(f"Files analysed: {len(outcome.paths)}")
    print(f"Text files: {text_count}")
    print(f"Notes with warnings: {warning_count}")
    print(f"Collection warnings: {len(outcome.collection_warnings)}")
    print(f"Failing notes: {failure_count}")
    print("\nValidation-excluded subtrees:")
    if target.ignored_dirs:
        for path in target.ignored_dirs:
            print(f"- {_display_path(path, repo_root=repo_root)}")
    else:
        print("- (none)")
    print("\nCollection structure:")
    if outcome.collection_structure:
        for _path, failure in outcome.collection_structure:
            print(f"- FAIL: {failure}")
    else:
        print("- PASS: no nested COLLECTION.md files")
    print("\nWarnings:")
    if warning_items:
        for path, warning in warning_items:
            print(f"- {_display_path(path, repo_root=repo_root)}: {warning}")
    else:
        print("- (none)")
    print("\nFailures:")
    if failure_items:
        for path, failure in failure_items:
            print(f"- {_display_path(path, repo_root=repo_root)}: {failure}")
    else:
        print("- (none)")
    print("\n===")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    output = parser.add_mutually_exclusive_group()
    output.add_argument(
        "--full",
        action="store_true",
        help="Print the complete per-artifact validation transcript.",
    )
    output.add_argument(
        "--json",
        action="store_true",
        help="Print a stable compact JSON result.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Atomically save the exact --json stdout bytes to this existing directory.",
    )
    parser.add_argument(
        "target",
        help=(
            "collection directory, note path or name, types, landings, redirects, "
            "lifecycle, or today/recent (kb/notes modified today)"
        ),
    )
    args = parser.parse_args(argv)
    if args.output is not None and not args.json:
        parser.error("--output requires --json")

    repo_root = Path.cwd().resolve()

    if args.target == "lifecycle":
        report = build_lifecycle_report(repo_root=repo_root)
        if args.json:
            emit_json_report(report, output_path=args.output)
        else:
            print(format_compact_report(report))
        return 1 if report.failure_count else 0

    if args.target == "redirects":
        results = validate_redirect_map(repo_root=repo_root)
        if args.full:
            print(format_block(repo_root / "properdocs.yml", results))
        else:
            report = build_single_validation_report(
                target_arg=args.target,
                path=repo_root / "properdocs.yml",
                results=results,
                repo_root=repo_root,
            )
            if args.json:
                emit_json_report(report, output_path=args.output)
            else:
                print(format_compact_report(report))
        return 1 if results.fails else 0

    if args.target == "landings":
        results = validate_collection_landings(repo_root=repo_root)
        if args.full:
            print(format_block(repo_root / "kb", results))
        else:
            report = build_single_validation_report(
                target_arg=args.target,
                path=repo_root / "kb",
                results=results,
                repo_root=repo_root,
            )
            if args.json:
                emit_json_report(report, output_path=args.output)
            else:
                print(format_compact_report(report))
        return 1 if results.fails else 0

    try:
        target = resolve_validation_target(args.target, repo_root=repo_root)
    except (FileNotFoundError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if not target.paths:
        print("No notes matched target.", file=sys.stderr)
        return 1

    outcome = run_validation(
        target.paths,
        repo_root=repo_root,
        collection=target.collection,
    )
    report = build_validation_report(
        target_arg=args.target,
        target=target,
        outcome=outcome,
        repo_root=repo_root,
    )
    if args.full:
        _print_full_collection_report(
            target=target,
            outcome=outcome,
            repo_root=repo_root,
        )
    elif args.json:
        emit_json_report(report, output_path=args.output)
    else:
        print(format_compact_report(report))

    return 1 if report.failure_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
