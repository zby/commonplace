"""Relocate KB notes and directories while preserving markdown links."""

from __future__ import annotations

import os
import re
import subprocess
import sys
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from commonplace.lib.naming import ensure_note_slug_length, slugify_note_filename
from commonplace.lib.project_paths import (
    find_repo_markdown_files,
    kb_root as project_kb_root,
    resolve_note as resolve_project_note,
)


TOKEN_PATTERN = re.compile(
    r"(```.*?```|`[^`\n]+`)|(\[([^\]]+)\]\(([^)]+)\))",
    flags=re.DOTALL,
)
EXTERNAL_TARGET = re.compile(r"^[a-z][a-z0-9+.-]*:")
REDIRECT_MAP_HEADER = re.compile(r"^(\s*)redirect_maps:\s*$")
REDIRECT_ENTRY = re.compile(r"^\s*['\"]([^'\"]+)['\"]:\s+['\"]([^'\"]+)['\"]\s*$")


@dataclass(frozen=True)
class NotePathMove:
    old_path: Path
    new_path: Path


class RelocationHook(Protocol):
    def plan(self, *, root: Path, moves: Sequence[NotePathMove]) -> object | None:
        """Return an opaque hook plan, or None when the hook has no work."""
        ...

    def execute(self, plan: object) -> None:
        """Execute hook work after the core relocation has written its changes."""
        ...

    def describe(self, plan: object) -> list[str]:
        """Return human-readable dry-run/apply output for a hook plan."""
        ...


def plan_hooks(
    hooks: Sequence[RelocationHook] | None,
    *,
    root: Path,
    moves: Sequence[NotePathMove],
) -> list[tuple[RelocationHook, object]]:
    plans: list[tuple[RelocationHook, object]] = []
    for hook in hooks or []:
        plan = hook.plan(root=root, moves=moves)
        if plan is not None:
            plans.append((hook, plan))
    return plans


def describe_hook_plans(plans: Sequence[tuple[RelocationHook, object]]) -> list[str]:
    lines: list[str] = []
    for hook, plan in plans:
        lines.extend(hook.describe(plan))
    return lines


def execute_hook_plans(plans: Sequence[tuple[RelocationHook, object]]) -> None:
    for hook, plan in plans:
        hook.execute(plan)


def resolve_note(arg: str, *, root: Path) -> Path:
    return resolve_project_note(arg, root)


def resolve_destination_dir(arg: str, *, repo_root: Path, kb_root: Path) -> Path:
    path = Path(arg)
    resolved = path.resolve() if path.is_absolute() else (repo_root / path).resolve()
    if kb_root != resolved and kb_root not in resolved.parents:
        raise ValueError(f"Destination directory must live under {kb_root}: {resolved}")
    return resolved


def resolve_destination_path(
    source: Path,
    new_name: str | None,
    dest_path: str | None,
    *,
    repo_root: Path,
    kb_root: Path,
) -> Path:
    if dest_path and new_name:
        raise ValueError("Use either --to or the [new_name] form, not both")

    if dest_path:
        raw = Path(dest_path)
        resolved = raw.resolve() if raw.is_absolute() else (repo_root / raw).resolve()
        if resolved.suffix == ".md":
            if kb_root not in resolved.parents:
                raise ValueError(f"Destination path must live under {kb_root}: {resolved}")
            ensure_note_slug_length(resolved.stem)
            return resolved

        directory = resolve_destination_dir(dest_path, repo_root=repo_root, kb_root=kb_root)
        return directory / source.name

    filename = source.name if new_name is None else f"{slugify_note_filename(new_name)}.md"
    return source.parent / filename


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

    def replace_match(match: re.Match[str]) -> str:
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

    return TOKEN_PATTERN.sub(replace_match, content), changes


def rebase_relative_markdown_links(
    content: str,
    old_source_file: Path,
    new_source_file: Path,
) -> tuple[str, list[str]]:
    changes: list[str] = []
    old_source_resolved = old_source_file.resolve()
    new_source_resolved = new_source_file.resolve()

    def replace_match(match: re.Match[str]) -> str:
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

    return TOKEN_PATTERN.sub(replace_match, content), changes


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
        raise ValueError("No redirect_maps section found in mkdocs config")

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


def move_path(source: Path, destination: Path, *, repo_root: Path) -> str:
    destination.parent.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(
            [
                "git",
                "mv",
                str(source.relative_to(repo_root)),
                str(destination.relative_to(repo_root)),
            ],
            cwd=repo_root,
            check=True,
            capture_output=True,
            text=True,
        )
        return "git mv"
    except (FileNotFoundError, subprocess.CalledProcessError):
        source.rename(destination)
        return "rename"


def move_note(source: Path, destination: Path, *, repo_root: Path) -> str:
    return move_path(source, destination, repo_root=repo_root)


def resolve_directory(arg: str, *, repo_root: Path, kb_root: Path) -> Path:
    """Resolve a directory path argument to an absolute path under kb/."""
    path = Path(arg)
    resolved = path.resolve() if path.is_absolute() else (repo_root / path).resolve()
    if not resolved.is_dir():
        raise FileNotFoundError(f"Source directory does not exist: {resolved}")
    if kb_root not in resolved.parents:
        raise FileNotFoundError(f"Directory must live under {kb_root}: {resolved}")
    return resolved


def rewrite_links_to_moved_files(
    content: str,
    source_file: Path,
    moves: dict[Path, Path],
) -> tuple[str, list[str]]:
    """Rewrite all links in `content` that point to any key in `moves`."""
    changes: list[str] = []

    def replace_match(match: re.Match[str]) -> str:
        if match.group(1):
            return match.group(0)

        text = match.group(3)
        target = match.group(4)
        if not text or not target or not is_relative_markdown_target(target):
            return match.group(0)

        bare_target, anchor = split_link_target(target)
        resolved = (source_file.parent / bare_target).resolve()
        if resolved not in moves:
            return match.group(0)

        new_path = moves[resolved]
        new_target = format_relative_link(source_file, new_path)
        if anchor:
            new_target = f"{new_target}{anchor}"
        changes.append(f"{target} -> {new_target}")
        return f"[{text}]({new_target})"

    return TOKEN_PATTERN.sub(replace_match, content), changes


def rebase_and_rewrite_in_moved_file(
    content: str,
    old_source_file: Path,
    new_source_file: Path,
    moves: dict[Path, Path],
) -> tuple[str, list[str]]:
    """Rewrite links inside a moved file.

    Handles two cases:
    - Links to other files in the same moved directory: update both the
      source position (since our file moved) and recognize the target is
      also in `moves` so the resolved path becomes the target's new location.
    - Links to files outside the moved directory: rebase for the new
      source position.
    """
    changes: list[str] = []

    def replace_match(match: re.Match[str]) -> str:
        if match.group(1):
            return match.group(0)

        text = match.group(3)
        target = match.group(4)
        if not text or not target or not is_relative_markdown_target(target):
            return match.group(0)

        bare_target, anchor = split_link_target(target)
        resolved = (old_source_file.parent / bare_target).resolve()

        if resolved in moves:
            destination = moves[resolved]
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

    return TOKEN_PATTERN.sub(replace_match, content), changes


def add_single_redirect(
    content: str,
    old_docs_path: str,
    new_docs_path: str,
) -> tuple[str, list[str]]:
    """Add or update a single redirect entry in mkdocs config."""
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
        rebuilt_lines.append(line)
        index += 1

    if redirects is None or header_index is None:
        raise ValueError("No redirect_maps section found in mkdocs config")

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


def relocate_directory(
    *,
    root: Path,
    source_arg: str,
    dest_path: str,
    redirect_from: str | None = None,
    redirect_to: str | None = None,
    apply: bool = False,
    hooks: Sequence[RelocationHook] | None = None,
) -> int:
    repo_root = root.resolve()
    kb_root = project_kb_root(repo_root)
    mkdocs_config = repo_root / "mkdocs.yml"

    source = resolve_directory(source_arg, repo_root=repo_root, kb_root=kb_root)

    # Destination may not exist yet
    dest = Path(dest_path)
    destination = dest.resolve() if dest.is_absolute() else (repo_root / dest).resolve()
    if kb_root not in destination.parents and destination != kb_root:
        print(f"Destination must live under {kb_root}: {destination}", file=sys.stderr)
        return 1
    if destination.exists():
        print(f"Destination already exists: {destination.relative_to(repo_root)}", file=sys.stderr)
        return 1

    # Collect moved file map (old_path -> new_path) for all files under source
    moves: dict[Path, Path] = {}
    for f in source.rglob("*"):
        if not f.is_file():
            continue
        rel = f.relative_to(source)
        moves[f.resolve()] = (destination / rel).resolve()

    md_moves = {k: v for k, v in moves.items() if k.suffix == ".md"}
    note_moves = [
        NotePathMove(old_path=old_path, new_path=new_path)
        for old_path, new_path in sorted(md_moves.items())
    ]
    try:
        hook_plans = plan_hooks(hooks, root=repo_root, moves=note_moves)
    except Exception as exc:
        print(f"Hook preflight failed: {exc}", file=sys.stderr)
        return 1

    # Rewrite links across the repo
    markdown_updates: dict[Path, tuple[Path, str, list[str]]] = {}
    for md_file in find_repo_markdown_files(repo_root):
        original = md_file.read_text(encoding="utf-8")
        md_resolved = md_file.resolve()
        if md_resolved in md_moves:
            new_path = md_moves[md_resolved]
            updated, changes = rebase_and_rewrite_in_moved_file(
                original, md_file, new_path, md_moves
            )
            target = new_path
        else:
            updated, changes = rewrite_links_to_moved_files(original, md_file, md_moves)
            target = md_file
        if changes:
            markdown_updates[md_file] = (target, updated, changes)

    # Optional single redirect entry
    mkdocs_changes: list[str] = []
    mkdocs_updated = None
    if redirect_from and redirect_to:
        mkdocs_original = mkdocs_config.read_text(encoding="utf-8")
        mkdocs_updated, mkdocs_changes = add_single_redirect(
            mkdocs_original, redirect_from, redirect_to
        )

    # Report
    mode = "APPLYING" if apply else "DRY RUN"
    print(f"=== {mode} ===\n")
    print(f"Relocate directory: {source.relative_to(repo_root)} -> {destination.relative_to(repo_root)}")
    print(f"Files to move: {len(moves)} ({len(md_moves)} markdown)")

    if markdown_updates:
        print(f"Markdown files to update: {len(markdown_updates)}")
        for path in sorted(markdown_updates):
            _, _, changes = markdown_updates[path]
            print(f"- {path.relative_to(repo_root)} ({len(changes)} link(s))")
    else:
        print("Markdown files to update: 0")

    if mkdocs_changes:
        print("MkDocs updates:")
        for change in mkdocs_changes:
            print(f"- {change}")
    else:
        print("MkDocs updates: none")

    for line in describe_hook_plans(hook_plans):
        print(line)

    if not apply:
        print("\nThis was a dry run. Pass --apply to execute.")
        return 0

    # Execute: git mv the whole directory
    try:
        subprocess.run(
            [
                "git",
                "mv",
                str(source.relative_to(repo_root)),
                str(destination.relative_to(repo_root)),
            ],
            cwd=repo_root,
            check=True,
            capture_output=True,
            text=True,
        )
        strategy = "git mv"
    except (FileNotFoundError, subprocess.CalledProcessError):
        destination.parent.mkdir(parents=True, exist_ok=True)
        source.rename(destination)
        strategy = "rename"

    # Write updated markdown files (targets reflect post-move locations)
    for _, (target, updated, _changes) in markdown_updates.items():
        target.write_text(updated, encoding="utf-8")

    # mkdocs config
    if mkdocs_updated is not None:
        mkdocs_config.write_text(mkdocs_updated, encoding="utf-8")

    try:
        execute_hook_plans(hook_plans)
    except Exception as exc:
        print(f"Hook execution failed after core relocation: {exc}", file=sys.stderr)
        return 1

    print(f"\nMove strategy: {strategy}")
    print("Done.")
    return 0


def relocate_note(
    *,
    root: Path,
    note_arg: str,
    new_name: str | None = None,
    dest_path: str | None = None,
    apply: bool = False,
    hooks: Sequence[RelocationHook] | None = None,
) -> int:
    repo_root = root.resolve()
    kb_root = project_kb_root(repo_root)
    mkdocs_config = repo_root / "mkdocs.yml"

    source = resolve_note(note_arg, root=repo_root)
    destination = resolve_destination_path(
        source,
        new_name,
        dest_path,
        repo_root=repo_root,
        kb_root=kb_root,
    )

    if destination == source:
        print(f"Destination matches source: {source.relative_to(repo_root)}", file=sys.stderr)
        return 1
    if destination.exists():
        print(f"Destination already exists: {destination.relative_to(repo_root)}", file=sys.stderr)
        return 1

    old_docs_path = source.relative_to(kb_root).as_posix()
    new_docs_path = destination.relative_to(kb_root).as_posix()
    try:
        hook_plans = plan_hooks(
            hooks,
            root=repo_root,
            moves=[NotePathMove(old_path=source, new_path=destination)],
        )
    except Exception as exc:
        print(f"Hook preflight failed: {exc}", file=sys.stderr)
        return 1

    markdown_updates: dict[Path, tuple[str, list[str]]] = {}

    for md_file in find_repo_markdown_files(repo_root):
        original = md_file.read_text(encoding="utf-8")
        if md_file.resolve() == source:
            updated, changes = rebase_relative_markdown_links(original, source, destination)
        else:
            updated, changes = rewrite_links_to_relocated_note(original, md_file, source, destination)
        if changes:
            markdown_updates[md_file] = (updated, changes)

    mkdocs_original = mkdocs_config.read_text(encoding="utf-8")
    mkdocs_updated, mkdocs_changes = update_mkdocs_config(
        mkdocs_original,
        old_docs_path=old_docs_path,
        new_docs_path=new_docs_path,
    )

    mode = "APPLYING" if apply else "DRY RUN"
    print(f"=== {mode} ===\n")
    print(f"Relocate: {source.relative_to(repo_root)} -> {destination.relative_to(repo_root)}")

    if markdown_updates:
        print(f"Markdown files to update: {len(markdown_updates)}")
        for path in sorted(markdown_updates):
            _, changes = markdown_updates[path]
            print(f"- {path.relative_to(repo_root)} ({len(changes)} link(s))")
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

    for line in describe_hook_plans(hook_plans):
        print(line)

    if not apply:
        print("\nThis was a dry run. Pass --apply to execute.")
        return 0

    strategy = move_note(source, destination, repo_root=repo_root)
    for path, (updated, _changes) in markdown_updates.items():
        target = destination if path.resolve() == source else path
        target.write_text(updated, encoding="utf-8")
    mkdocs_config.write_text(mkdocs_updated, encoding="utf-8")
    try:
        execute_hook_plans(hook_plans)
    except Exception as exc:
        print(f"Hook execution failed after core relocation: {exc}", file=sys.stderr)
        return 1

    print(f"\nMove strategy: {strategy}")
    print("Done.")
    return 0
