"""Deterministic validator for KB notes."""

from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

from commonplace.lib.type_resolver import check_type_uniqueness
from commonplace.lib.validation import (
    CheckResults,
    list_kb_note_paths,
    orphan_info,
    validate_note,
)


def resolve_targets(arg: str, *, repo_root: Path, notes_root: Path) -> list[Path]:
    if arg in {"all", "notes"}:
        return list_kb_note_paths(notes_root)

    if arg in {"recent", "today"}:
        today = datetime.now().date()
        return sorted(
            path
            for path in list_kb_note_paths(notes_root)
            if datetime.fromtimestamp(path.stat().st_mtime).date() == today
        )

    candidate = Path(arg)
    if candidate.is_file():
        return [candidate.resolve()]

    repo_candidate = (repo_root / arg).resolve()
    if repo_candidate.is_file():
        return [repo_candidate]

    name = arg if arg.endswith(".md") else f"{arg}.md"
    matches = sorted(path for path in notes_root.rglob(name))
    if not matches:
        matches = sorted(path for path in notes_root.rglob("*.md") if path.stem == arg)

    if not matches:
        raise FileNotFoundError(f"No matching note found for: {arg}")
    if len(matches) > 1:
        raise FileNotFoundError(
            "Multiple matching notes found:\n" + "\n".join(str(path.relative_to(repo_root)) for path in matches)
        )
    return matches


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
    parser.add_argument("target", help="note path, note name, all, or recent")
    args = parser.parse_args(argv)

    repo_root = Path.cwd().resolve()
    notes_root = repo_root / "kb" / "notes"

    try:
        paths = resolve_targets(args.target, repo_root=repo_root, notes_root=notes_root)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if not paths:
        print("No notes matched target.", file=sys.stderr)
        return 1

    inbound = orphan_info(paths) if args.target in {"all", "notes"} else {}
    had_failures = False
    text_count = 0
    warning_count = 0
    failure_count = 0
    warning_items: list[tuple[Path, str]] = []
    failure_items: list[tuple[Path, str]] = []

    for path in paths:
        results = validate_note(path, repo_root=repo_root)
        if results.note_type == "text":
            text_count += 1
        if args.target in {"all", "notes"} and path in inbound and not inbound[path] and results.note_type != "text":
            results.infos.append("orphan check: no inbound links found in kb/notes")
        print(format_block(path, results))
        if results.warns:
            warning_count += 1
            warning_items.extend((path, warning) for warning in results.warns)
        if results.fails:
            had_failures = True
            failure_count += 1
            failure_items.extend((path, failure) for failure in results.fails)

    if args.target in {"all", "notes"}:
        type_warnings = check_type_uniqueness(repo_root)
        if type_warnings:
            had_failures = True

        print("\n=== BATCH INFO ===\n")
        print(f"Files analysed: {len(paths)}")
        print(f"Text files: {text_count}")
        print(f"Notes with warnings: {warning_count}")
        print(f"Failing notes: {failure_count}")
        print("\nType system:")
        if type_warnings:
            for tw in type_warnings:
                print(f"- FAIL: {tw}")
        else:
            print("- PASS: all type names are globally unique")
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
