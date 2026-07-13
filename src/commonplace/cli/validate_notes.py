"""Deterministic validator for KB notes."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from commonplace.lib.project_paths import (
    kb_root,
    list_collection_note_paths,
    list_notes_collection_paths,
    list_type_spec_paths,
    resolve_note,
)
from commonplace.lib.validation import (
    CheckResults,
    run_validation,
)


_TOO_BROAD_MESSAGE = (
    "Validation scope must be a specific collection or file. "
    "Pass one of: notes, types, reference, instructions, agent-memory-systems, "
    "sources, or a note path."
)


@dataclass(frozen=True)
class ResolvedValidationTarget:
    paths: tuple[Path, ...]
    collection: Path | None = None


def _collection_target(collection: Path) -> ResolvedValidationTarget:
    resolved = collection.resolve()
    return ResolvedValidationTarget(
        paths=tuple(list_collection_note_paths(resolved)),
        collection=resolved,
    )


def resolve_validation_target(
    arg: str, *, repo_root: Path
) -> ResolvedValidationTarget:
    if arg == "all":
        raise ValueError(_TOO_BROAD_MESSAGE)
    if arg == "notes":
        collection = (kb_root(repo_root) / "notes").resolve()
        return ResolvedValidationTarget(
            paths=tuple(list_notes_collection_paths(repo_root)),
            collection=collection,
        )
    if arg == "types":
        return ResolvedValidationTarget(paths=tuple(list_type_spec_paths(repo_root)))

    if arg in {"recent", "today"}:
        today = datetime.now().date()
        return ResolvedValidationTarget(
            paths=tuple(
                sorted(
                    path
                    for path in list_notes_collection_paths(repo_root)
                    if datetime.fromtimestamp(path.stat().st_mtime).date() == today
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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "target",
        help=(
            "collection directory, note path or name, types, or today/recent "
            "(kb/notes modified today)"
        ),
    )
    args = parser.parse_args(argv)

    repo_root = Path.cwd().resolve()

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
    paths = list(outcome.paths)

    scope = (
        _display_path(target.collection, repo_root=repo_root)
        if target.collection is not None
        else None
    )
    had_failures = False
    text_count = 0
    warning_count = 0
    failure_count = 0
    warning_items: list[tuple[Path, str]] = []
    failure_items: list[tuple[Path, str]] = []

    for path in paths:
        results = outcome.results[path]
        if results.note_type == "text":
            text_count += 1
        print(format_block(path, results))
        if results.warns:
            warning_count += 1
            warning_items.extend((path, warning) for warning in results.warns)
        if results.fails:
            had_failures = True
            failure_count += 1
            failure_items.extend((path, failure) for failure in results.fails)

    if scope is not None:
        structure_failures = outcome.collection_structure
        if structure_failures:
            had_failures = True

        print("\n=== BATCH INFO ===\n")
        print(f"Files analysed: {len(paths)}")
        print(f"Text files: {text_count}")
        print(f"Notes with warnings: {warning_count}")
        print(f"Failing notes: {failure_count}")
        print("\nCollection structure:")
        if structure_failures:
            for _path, failure in structure_failures:
                print(f"- FAIL: {failure}")
        else:
            print("- PASS: no nested COLLECTION.md files")
        print("\nWarnings:")
        if warning_items:
            for path, warning in warning_items:
                print(f"- {path.relative_to(repo_root)}: {warning}")
        else:
            print("- (none)")
        print("\nFailures:")
        if failure_items:
            for path, failure in failure_items:
                print(f"- {path.relative_to(repo_root)}: {failure}")
        else:
            print("- (none)")
        print("\n===")

    return 1 if had_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
