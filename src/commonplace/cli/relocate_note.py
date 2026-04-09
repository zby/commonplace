#!/usr/bin/env python3
"""Relocate a KB note by renaming it, moving it, or both.

Usage:
    commonplace-relocate-note kb/notes/my-note.md "New note title"
    commonplace-relocate-note kb/notes/my-note.md --dir kb/notes/definitions
    commonplace-relocate-note kb/notes/my-note.md --to kb/notes/definitions/new-note.md --apply
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

from commonplace.lib.naming import ensure_note_slug_length, slugify_note_filename


REPO_ROOT = Path.cwd().resolve()
KB_ROOT = REPO_ROOT / "kb"
NOTES_ROOT = KB_ROOT / "notes"
MKDOCS_CONFIG = REPO_ROOT / "mkdocs.yml"
TOKEN_PATTERN = re.compile(
    r"(```.*?```|`[^`\n]+`)|(\[([^\]]+)\]\(([^)]+)\))",
    flags=re.DOTALL,
)
EXTERNAL_TARGET = re.compile(r"^[a-z][a-z0-9+.-]*:")
REDIRECT_MAP_HEADER = re.compile(r"^(\s*)redirect_maps:\s*$")
REDIRECT_ENTRY = re.compile(r"^\s*['\"]([^'\"]+)['\"]:\s+['\"]([^'\"]+)['\"]\s*$")


def slugify(text: str) -> str:
    return slugify_note_filename(text)


def is_nested_git_repo_content(path: Path) -> bool:
    current = path.parent
    while current != REPO_ROOT and REPO_ROOT in current.parents:
        if (current / ".git").exists():
            return True
        current = current.parent
    return False


def resolve_note(arg: str) -> Path:
    candidate = Path(arg)
    if candidate.is_file():
        resolved = candidate.resolve()
        if NOTES_ROOT not in resolved.parents:
            raise FileNotFoundError(f"Note must live under {NOTES_ROOT}: {resolved}")
        return resolved

    repo_candidate = (REPO_ROOT / arg).resolve()
    if repo_candidate.is_file():
        if NOTES_ROOT not in repo_candidate.parents:
            raise FileNotFoundError(f"Note must live under {NOTES_ROOT}: {repo_candidate}")
        return repo_candidate

    name = arg if arg.endswith(".md") else f"{arg}.md"
    matches = sorted(path.resolve() for path in NOTES_ROOT.rglob(name))
    if not matches:
        matches = sorted(path.resolve() for path in NOTES_ROOT.rglob("*.md") if path.stem == arg)

    if not matches:
        raise FileNotFoundError(f"No matching note found for: {arg}")
    if len(matches) > 1:
        formatted = "\n".join(str(path.relative_to(REPO_ROOT)) for path in matches)
        raise FileNotFoundError(f"Multiple matching notes found:\n{formatted}")
    return matches[0]


def resolve_destination_dir(arg: str) -> Path:
    path = Path(arg)
    resolved = path.resolve() if path.is_absolute() else (REPO_ROOT / path).resolve()
    if NOTES_ROOT != resolved and NOTES_ROOT not in resolved.parents:
        raise ValueError(f"Destination directory must live under {NOTES_ROOT}: {resolved}")
    return resolved


def resolve_destination_path(source: Path, new_name: str | None, dest_dir: str | None, dest_path: str | None) -> Path:
    if dest_path and (new_name or dest_dir):
        raise ValueError("Use either --to or the [new_name] / --dir form, not both")

    if dest_path:
        raw = Path(dest_path)
        resolved = raw.resolve() if raw.is_absolute() else (REPO_ROOT / raw).resolve()
        if resolved.suffix != ".md":
            raise ValueError(f"Destination path must end with .md: {resolved}")
        if NOTES_ROOT not in resolved.parents:
            raise ValueError(f"Destination path must live under {NOTES_ROOT}: {resolved}")
        ensure_note_slug_length(resolved.stem)
        return resolved

    filename = source.name if new_name is None else f"{slugify(new_name)}.md"
    directory = source.parent if dest_dir is None else resolve_destination_dir(dest_dir)
    return directory / filename


def format_relative_link(from_file: Path, to_file: Path) -> str:
    rel = os.path.relpath(to_file, from_file.parent)
    return rel if rel.startswith("..") else f"./{rel}"


def iter_markdown_tokens(content: str):
    for match in TOKEN_PATTERN.finditer(content):
        if match.group(1):
            continue
        text = match.group(3)
        target = match.group(4)
        if text and target:
            yield match, text, target


def split_link_target(target: str) -> tuple[str, str]:
    if "#" in target:
        bare, anchor = target.rsplit("#", 1)
        return bare, f"#{anchor}"
    return target, ""


def is_relative_markdown_target(target: str) -> bool:
    bare, _anchor = split_link_target(target)
    if bare.startswith("#") or not bare:
        return False
    if EXTERNAL_TARGET.match(bare):
        return False
    return bare.endswith(".md")


def rewrite_links_to_relocated_note(
    content: str,
    source_file: Path,
    old_path: Path,
    new_path: Path,
) -> tuple[str, list[str]]:
    changes: list[str] = []
    old_resolved = old_path.resolve()

    def replace(match: re.Match[str]) -> str:
        if match.group(1):
            return match.group(0)

        text = match.group(3)
        target = match.group(4)
        if not text or not target or not is_relative_markdown_target(target):
            return match.group(0)

        bare_target, anchor = split_link_target(target)
        resolved = (source_file.parent / bare_target).resolve()
        if resolved != old_resolved:
            return match.group(0)

        new_target = format_relative_link(source_file, new_path)
        if anchor:
            new_target = f"{new_target}{anchor}"
        changes.append(f"{target} -> {new_target}")
        return f"[{text}]({new_target})"

    return TOKEN_PATTERN.sub(replace, content), changes


def rebase_relative_markdown_links(
    content: str,
    old_source_file: Path,
    new_source_file: Path,
) -> tuple[str, list[str]]:
    changes: list[str] = []
    old_source_resolved = old_source_file.resolve()
    new_source_resolved = new_source_file.resolve()

    def replace(match: re.Match[str]) -> str:
        if match.group(1):
            return match.group(0)

        text = match.group(3)
        target = match.group(4)
        if not text or not target or not is_relative_markdown_target(target):
            return match.group(0)

        bare_target, anchor = split_link_target(target)
        resolved = (old_source_file.parent / bare_target).resolve()
        if resolved == old_source_resolved:
            destination = new_source_resolved
        elif resolved.exists():
            destination = resolved
        else:
            return match.group(0)

        new_target = format_relative_link(new_source_file, destination)
        if anchor:
            new_target = f"{new_target}{anchor}"
        if new_target == target:
            return match.group(0)
        changes.append(f"{target} -> {new_target}")
        return f"[{text}]({new_target})"

    return TOKEN_PATTERN.sub(replace, content), changes


def find_repo_markdown_files() -> list[Path]:
    return sorted(
        path
        for path in REPO_ROOT.rglob("*.md")
        if not is_nested_git_repo_content(path.resolve())
    )


def update_mkdocs_config(
    content: str,
    old_docs_path: str,
    new_docs_path: str,
) -> tuple[str, list[str]]:
    lines = content.splitlines()
    rebuilt_lines: list[str] = []
    changes: list[str] = []
    redirects: dict[str, str] | None = None
    header_index: int | None = None
    header_indent = 0
    entry_indent: int | None = None
    index = 0

    while index < len(lines):
        line = lines[index]
        header_match = REDIRECT_MAP_HEADER.match(line)
        if header_match:
            redirects = {}
            header_index = len(rebuilt_lines)
            header_indent = len(header_match.group(1))
            rebuilt_lines.append(line)
            index += 1

            while index < len(lines):
                candidate = lines[index]
                stripped = candidate.strip()
                indent = len(candidate) - len(candidate.lstrip(" "))
                if stripped and indent <= header_indent:
                    break
                if stripped:
                    entry_match = REDIRECT_ENTRY.match(candidate)
                    if not entry_match:
                        raise ValueError(f"Unsupported redirect_maps entry: {candidate}")
                    redirects[entry_match.group(1)] = entry_match.group(2)
                    entry_indent = indent
                index += 1
            continue

        updated_line = re.sub(
            rf"(:\s*)(['\"]?){re.escape(old_docs_path)}\2(\s*(?:#.*)?)$",
            lambda match: f"{match.group(1)}{match.group(2)}{new_docs_path}{match.group(2)}{match.group(3)}",
            line,
        )
        if updated_line != line:
            changes.append(f"mkdocs value: {old_docs_path} -> {new_docs_path}")
        rebuilt_lines.append(updated_line)
        index += 1

    if redirects is None or header_index is None:
        raise ValueError(f"No redirect_maps section found in {MKDOCS_CONFIG}")

    for key, value in list(redirects.items()):
        if value == old_docs_path and key != old_docs_path:
            redirects[key] = new_docs_path
            changes.append(f"mkdocs redirect target: {key} -> {new_docs_path}")

    if redirects.get(old_docs_path) != new_docs_path:
        redirects[old_docs_path] = new_docs_path
        changes.append(f"mkdocs redirect: {old_docs_path} -> {new_docs_path}")

    indent = entry_indent if entry_indent is not None else header_indent + 2
    redirect_lines = [f'{" " * header_indent}redirect_maps:']
    for key in sorted(redirects, key=str.casefold):
        redirect_lines.append(f'{" " * indent}\'{key}\': \'{redirects[key]}\'')
    rebuilt_lines[header_index : header_index + 1] = redirect_lines

    new_content = "\n".join(rebuilt_lines)
    if content.endswith("\n"):
        new_content += "\n"
    return new_content, changes


def move_note(source: Path, destination: Path) -> str:
    destination.parent.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(
            [
                "git",
                "mv",
                str(source.relative_to(REPO_ROOT)),
                str(destination.relative_to(REPO_ROOT)),
            ],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        return "git mv"
    except (FileNotFoundError, subprocess.CalledProcessError):
        source.rename(destination)
        return "rename"


def relocate_note(
    note_arg: str,
    new_name: str | None = None,
    *,
    dest_dir: str | None = None,
    dest_path: str | None = None,
    apply: bool = False,
) -> int:
    source = resolve_note(note_arg)
    destination = resolve_destination_path(source, new_name, dest_dir, dest_path)

    if destination == source:
        print(f"Destination matches source: {source.relative_to(REPO_ROOT)}", file=sys.stderr)
        return 1
    if destination.exists():
        print(f"Destination already exists: {destination.relative_to(REPO_ROOT)}", file=sys.stderr)
        return 1

    old_docs_path = source.relative_to(KB_ROOT).as_posix()
    new_docs_path = destination.relative_to(KB_ROOT).as_posix()
    markdown_updates: dict[Path, tuple[str, list[str]]] = {}

    for md_file in find_repo_markdown_files():
        original = md_file.read_text(encoding="utf-8")
        if md_file.resolve() == source:
            updated, changes = rebase_relative_markdown_links(original, source, destination)
        else:
            updated, changes = rewrite_links_to_relocated_note(original, md_file, source, destination)
        if changes:
            markdown_updates[md_file] = (updated, changes)

    mkdocs_original = MKDOCS_CONFIG.read_text(encoding="utf-8")
    mkdocs_updated, mkdocs_changes = update_mkdocs_config(
        mkdocs_original,
        old_docs_path=old_docs_path,
        new_docs_path=new_docs_path,
    )

    mode = "APPLYING" if apply else "DRY RUN"
    print(f"=== {mode} ===\n")
    print(f"Relocate: {source.relative_to(REPO_ROOT)} -> {destination.relative_to(REPO_ROOT)}")

    if markdown_updates:
        print(f"Markdown files to update: {len(markdown_updates)}")
        for path in sorted(markdown_updates):
            _, changes = markdown_updates[path]
            print(f"- {path.relative_to(REPO_ROOT)} ({len(changes)} link(s))")
            for change in changes:
                print(f"  {change}")
    else:
        print("Markdown files to update: 0")

    if mkdocs_changes:
        print("MkDocs updates:")
        for change in mkdocs_changes:
            print(f"- {change}")
    else:
        print("MkDocs updates: none")

    if not apply:
        print("\nThis was a dry run. Pass --apply to execute.")
        return 0

    strategy = move_note(source, destination)
    for path, (updated, _changes) in markdown_updates.items():
        target = destination if path.resolve() == source else path
        target.write_text(updated, encoding="utf-8")
    MKDOCS_CONFIG.write_text(mkdocs_updated, encoding="utf-8")

    print(f"\nMove strategy: {strategy}")
    print("Done.")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("note", help="Note path or unique note name under kb/notes/")
    parser.add_argument("new_name", nargs="?", help="New title or filename stem; omit to keep the current filename")
    parser.add_argument("--dir", dest="dest_dir", help="Destination directory under kb/notes/")
    parser.add_argument("--to", dest="dest_path", help="Full destination .md path under kb/notes/")
    parser.add_argument("--apply", action="store_true", help="Write changes instead of dry-running")
    args = parser.parse_args()

    try:
        sys.exit(
            relocate_note(
                args.note,
                args.new_name,
                dest_dir=args.dest_dir,
                dest_path=args.dest_path,
                apply=args.apply,
            )
        )
    except (FileNotFoundError, ValueError) as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
