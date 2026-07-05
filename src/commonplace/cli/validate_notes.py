"""Deterministic validator for KB notes."""

from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

from commonplace.lib.project_paths import (
    collection_for_path,
    is_collection_dir,
    is_type_definition_content,
    iter_visible_markdown_files,
    kb_root,
    list_collection_note_paths,
    list_kb_note_paths,
    list_notes_collection_paths,
)
from commonplace.lib.type_resolver import validate_type_specs
from commonplace.lib.validation import (
    CheckResults,
    orphan_info,
    parse_note,
    validate_note,
)


_TOO_BROAD_MESSAGE = (
    "Validation scope must be a specific collection or file. "
    "Pass one of: notes, reference, instructions, agent-memory-systems, sources, "
    "or a note path."
)


def resolve_targets(arg: str, *, repo_root: Path) -> list[Path]:
    if arg == "all":
        raise ValueError(_TOO_BROAD_MESSAGE)
    if arg == "notes":
        return list_notes_collection_paths(repo_root)

    if arg in {"recent", "today"}:
        today = datetime.now().date()
        return sorted(
            path
            for path in list_notes_collection_paths(repo_root)
            if datetime.fromtimestamp(path.stat().st_mtime).date() == today
        )

    kb = kb_root(repo_root).resolve()

    candidate = Path(arg)
    if candidate.is_absolute() and candidate.is_file():
        return [candidate.resolve()]
    if candidate.is_absolute() and candidate.is_dir():
        resolved = candidate.resolve()
        if resolved == kb:
            raise ValueError(_TOO_BROAD_MESSAGE)
        return list_collection_note_paths(resolved)

    repo_candidate = (repo_root / arg).resolve()
    if repo_candidate.is_file():
        return [repo_candidate]
    if repo_candidate.is_dir():
        if repo_candidate == kb:
            raise ValueError(_TOO_BROAD_MESSAGE)
        return list_collection_note_paths(repo_candidate)

    collection_candidate = (kb_root(repo_root) / arg).resolve()
    if collection_candidate.is_dir():
        if collection_candidate == kb:
            raise ValueError(_TOO_BROAD_MESSAGE)
        return list_collection_note_paths(collection_candidate)

    all_paths = list_kb_note_paths(repo_root)
    name = arg if arg.endswith(".md") else f"{arg}.md"
    matches = sorted(path for path in all_paths if path.name == name)
    if not matches:
        matches = sorted(path for path in all_paths if path.stem == arg)

    if not matches:
        raise FileNotFoundError(f"No matching note found for: {arg}")
    if len(matches) > 1:
        raise FileNotFoundError(
            "Multiple matching notes found:\n" + "\n".join(str(path.relative_to(repo_root)) for path in matches)
        )
    return matches


def _display_path(path: Path, *, repo_root: Path) -> str:
    try:
        return str(path.relative_to(repo_root))
    except ValueError:
        return str(path)


def batch_scope(arg: str, *, repo_root: Path) -> str | None:
    """Return a display label when the target should use batch reporting."""
    if arg == "notes":
        return "kb/notes"

    candidate = Path(arg)
    if candidate.is_absolute() and candidate.is_dir():
        resolved = candidate.resolve()
        return _display_path(resolved, repo_root=repo_root) if is_collection_dir(resolved) else None

    repo_candidate = (repo_root / arg).resolve()
    if repo_candidate.is_dir() and is_collection_dir(repo_candidate):
        return _display_path(repo_candidate, repo_root=repo_root)

    collection_candidate = (kb_root(repo_root) / arg).resolve()
    if collection_candidate.is_dir() and is_collection_dir(collection_candidate):
        return _display_path(collection_candidate, repo_root=repo_root)

    return None


def impacted_marked_tag_readmes(paths: list[Path], *, repo_root: Path) -> list[Path]:
    """Return marked tag READMEs whose claims may be affected by these notes."""
    seen = {path.resolve() for path in paths}
    impacted: list[Path] = []

    for path in paths:
        parsed, parse_error = parse_note(path, repo_root=repo_root)
        if parse_error or parsed is None or parsed.document.frontmatter is None:
            continue
        tags = parsed.document.frontmatter.get("tags")
        if not isinstance(tags, list):
            continue
        try:
            collection = collection_for_path(path, repo_root)
        except ValueError:
            continue

        for tag in tags:
            if not isinstance(tag, str):
                continue
            readme = (collection / f"{tag}-README.md").resolve()
            if not readme.is_file() or readme in seen:
                continue
            readme_parsed, readme_error = parse_note(readme, repo_root=repo_root)
            if readme_error or readme_parsed is None or readme_parsed.note_type != "tag-readme":
                continue
            fm = readme_parsed.document.frontmatter or {}
            has_checked_mark = fm.get("complete") is True or bool(fm.get("covered_by"))
            if not has_checked_mark:
                continue

            impacted.append(readme)
            seen.add(readme)

    return impacted


def validate_collection_structure(collection: Path, *, repo_root: Path) -> list[str]:
    """Return collection-level structural failures for a validation scope."""
    collection = collection.resolve()
    repo_root = repo_root.resolve()
    if not is_collection_dir(collection):
        return []

    failures: list[str] = []
    for path in iter_visible_markdown_files(collection):
        if path.name != "COLLECTION.md" or path.parent == collection:
            continue
        if is_type_definition_content(path, collection):
            continue
        failures.append(
            "nested COLLECTION.md: "
            f"{path.relative_to(repo_root)} is inside collection {collection.relative_to(repo_root)}"
        )
    return failures


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
    parser.add_argument("target", help="note path, directory, note name, all, or recent")
    args = parser.parse_args(argv)

    repo_root = Path.cwd().resolve()

    try:
        paths = resolve_targets(args.target, repo_root=repo_root)
    except (FileNotFoundError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if not paths:
        print("No notes matched target.", file=sys.stderr)
        return 1

    paths.extend(impacted_marked_tag_readmes(paths, repo_root=repo_root))

    scope = batch_scope(args.target, repo_root=repo_root)
    inbound = orphan_info(paths) if scope is not None else {}
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
        if scope is not None and path in inbound and not inbound[path] and results.note_type != "text":
            results.infos.append(f"orphan check: no inbound links found in {scope}")
        print(format_block(path, results))
        if results.warns:
            warning_count += 1
            warning_items.extend((path, warning) for warning in results.warns)
        if results.fails:
            had_failures = True
            failure_count += 1
            failure_items.extend((path, failure) for failure in results.fails)

    if scope is not None:
        type_failures = validate_type_specs(repo_root)
        if type_failures:
            had_failures = True
        structure_failures = validate_collection_structure(repo_root / scope, repo_root=repo_root)
        if structure_failures:
            had_failures = True

        print("\n=== BATCH INFO ===\n")
        print(f"Files analysed: {len(paths)}")
        print(f"Text files: {text_count}")
        print(f"Notes with warnings: {warning_count}")
        print(f"Failing notes: {failure_count}")
        print("\nType system:")
        if type_failures:
            for failure in type_failures:
                print(f"- FAIL: {failure}")
        else:
            print("- PASS: all type-spec docs are valid")
        print("\nCollection structure:")
        if structure_failures:
            for failure in structure_failures:
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
