"""Relocate KB notes and directories while preserving markdown links."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

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


class _RedirectMaps:
    """The parsed `redirect_maps:` section of a ProperDocs config.

    `lines` is the config with the whole section collapsed to its single
    header line at `header_index`; `render` expands it back with the current
    `redirects` mapping. `parsed` is False when the config has no section.
    """

    def __init__(self, content: str) -> None:
        self.redirects: dict[str, str] = {}
        self.lines: list[str] = []
        self.parsed = False
        self._header_index = 0
        self._header_indent = 0
        self._entry_indent: int | None = None
        self._trailing_newline = content.endswith("\n")

        source = content.splitlines()
        index = 0
        while index < len(source):
            line = source[index]
            header_match = REDIRECT_MAP_HEADER.match(line)
            if not header_match:
                self.lines.append(line)
                index += 1
                continue

            self.parsed = True
            self._header_index = len(self.lines)
            self._header_indent = len(header_match.group(1))
            self.lines.append(line)
            index += 1
            while index < len(source):
                candidate = source[index]
                stripped = candidate.strip()
                indent = len(candidate) - len(candidate.lstrip(" "))
                if stripped and indent <= self._header_indent:
                    break
                if stripped:
                    entry_match = REDIRECT_ENTRY.match(candidate)
                    if not entry_match:
                        raise ValueError(f"Unsupported redirect_maps entry: {candidate}")
                    self.redirects[entry_match.group(1)] = entry_match.group(2)
                    self._entry_indent = indent
                index += 1

    def add(self, old_docs_path: str, new_docs_path: str, changes: list[str]) -> None:
        if self.redirects.get(old_docs_path) != new_docs_path:
            self.redirects[old_docs_path] = new_docs_path
            changes.append(f"properdocs redirect: {old_docs_path} -> {new_docs_path}")

    def render(self) -> str:
        rebuilt = list(self.lines)
        if self.parsed:
            indent = (
                self._entry_indent
                if self._entry_indent is not None
                else self._header_indent + 2
            )
            redirect_lines = [f'{" " * self._header_indent}redirect_maps:']
            for key in sorted(self.redirects, key=str.casefold):
                redirect_lines.append(f"{' ' * indent}'{key}': '{self.redirects[key]}'")
            rebuilt[self._header_index : self._header_index + 1] = redirect_lines
        new_content = "\n".join(rebuilt)
        if self._trailing_newline:
            new_content += "\n"
        return new_content


def update_properdocs_config(
    content: str,
    old_docs_path: str,
    new_docs_path: str,
) -> tuple[str, list[str]]:
    """Rewrite doc-path values (nav entries etc.) and maintain the redirect map.

    A config without a `redirect_maps:` section still gets its values
    rewritten; the redirect entry is simply skipped, so projects that use
    ProperDocs without the redirects plugin can relocate notes.
    """
    changes: list[str] = []
    maps = _RedirectMaps(content)

    value_re = re.compile(
        rf"(:\s*)(['\"]?){re.escape(old_docs_path)}\2(\s*(?:#.*)?)$"
    )
    for index, line in enumerate(maps.lines):
        updated_line = value_re.sub(
            lambda match: f"{match.group(1)}{match.group(2)}{new_docs_path}{match.group(2)}{match.group(3)}",
            line,
        )
        if updated_line != line:
            changes.append(f"properdocs value: {old_docs_path} -> {new_docs_path}")
            maps.lines[index] = updated_line

    if maps.parsed:
        for key, value in list(maps.redirects.items()):
            if value == old_docs_path and key != old_docs_path:
                maps.redirects[key] = new_docs_path
                changes.append(f"properdocs redirect target: {key} -> {new_docs_path}")
        maps.add(old_docs_path, new_docs_path, changes)

    return maps.render(), changes


def move_path(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    source.rename(destination)


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
    """Add or update a single redirect entry in ProperDocs config."""
    maps = _RedirectMaps(content)
    if not maps.parsed:
        raise ValueError("No redirect_maps section found in ProperDocs config")
    changes: list[str] = []
    maps.add(old_docs_path, new_docs_path, changes)
    return maps.render(), changes


def relocate_directory(
    *,
    root: Path,
    source_arg: str,
    dest_path: str,
    redirect_from: str | None = None,
    redirect_to: str | None = None,
    apply: bool = False,
) -> int:
    repo_root = root.resolve()
    kb_root = project_kb_root(repo_root)
    properdocs_config = repo_root / "properdocs.yml"

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
    properdocs_changes: list[str] = []
    properdocs_updated = None
    if redirect_from and redirect_to:
        properdocs_original = properdocs_config.read_text(encoding="utf-8")
        properdocs_updated, properdocs_changes = add_single_redirect(
            properdocs_original, redirect_from, redirect_to
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

    if properdocs_changes:
        print("ProperDocs updates:")
        for change in properdocs_changes:
            print(f"- {change}")
    else:
        print("ProperDocs updates: none")

    if not apply:
        print("\nThis was a dry run. Pass --apply to execute.")
        return 0

    move_path(source, destination)

    # Write updated markdown files (targets reflect post-move locations)
    for _, (target, updated, _changes) in markdown_updates.items():
        target.write_text(updated, encoding="utf-8")

    # ProperDocs config
    if properdocs_updated is not None:
        properdocs_config.write_text(properdocs_updated, encoding="utf-8")

    print("\nDone.")
    return 0


def relocate_note(
    *,
    root: Path,
    note_arg: str,
    new_name: str | None = None,
    dest_path: str | None = None,
    apply: bool = False,
) -> int:
    repo_root = root.resolve()
    kb_root = project_kb_root(repo_root)
    properdocs_config = repo_root / "properdocs.yml"

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

    md_moves = {source: destination}
    markdown_updates: dict[Path, tuple[str, list[str]]] = {}

    for md_file in find_repo_markdown_files(repo_root):
        original = md_file.read_text(encoding="utf-8")
        if md_file.resolve() == source:
            updated, changes = rebase_and_rewrite_in_moved_file(
                original, md_file, destination, md_moves
            )
        else:
            updated, changes = rewrite_links_to_moved_files(original, md_file, md_moves)
        if changes:
            markdown_updates[md_file] = (updated, changes)

    # Projects without a ProperDocs site have nothing to update here.
    properdocs_updated = None
    properdocs_changes: list[str] = []
    if properdocs_config.is_file():
        properdocs_updated, properdocs_changes = update_properdocs_config(
            properdocs_config.read_text(encoding="utf-8"),
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

    if properdocs_changes:
        print("ProperDocs updates:")
        for change in properdocs_changes:
            print(f"- {change}")
    else:
        print("ProperDocs updates: none")

    if not apply:
        print("\nThis was a dry run. Pass --apply to execute.")
        return 0

    move_path(source, destination)
    for path, (updated, _changes) in markdown_updates.items():
        target = destination if path.resolve() == source else path
        target.write_text(updated, encoding="utf-8")
    if properdocs_updated is not None:
        properdocs_config.write_text(properdocs_updated, encoding="utf-8")
    print("\nDone.")
    return 0
