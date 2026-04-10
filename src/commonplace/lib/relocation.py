"""Relocate a KB note: rename, move, fix links, rewrite review exports, rekey the DB."""

from __future__ import annotations

import os
import re
import subprocess
import sys
from dataclasses import replace
from pathlib import Path

from commonplace.lib.naming import ensure_note_slug_length, slugify_note_filename
from commonplace.review import review_db, review_metadata


TOKEN_PATTERN = re.compile(
    r"(```.*?```|`[^`\n]+`)|(\[([^\]]+)\]\(([^)]+)\))",
    flags=re.DOTALL,
)
EXTERNAL_TARGET = re.compile(r"^[a-z][a-z0-9+.-]*:")
REDIRECT_MAP_HEADER = re.compile(r"^(\s*)redirect_maps:\s*$")
REDIRECT_ENTRY = re.compile(r"^\s*['\"]([^'\"]+)['\"]:\s+['\"]([^'\"]+)['\"]\s*$")


def is_nested_git_repo_content(path: Path, repo_root: Path) -> bool:
    current = path.parent
    while current != repo_root and repo_root in current.parents:
        if (current / ".git").exists():
            return True
        current = current.parent
    return False


def resolve_note(arg: str, *, repo_root: Path, kb_root: Path) -> Path:
    candidate = Path(arg)
    if candidate.is_absolute() and candidate.is_file():
        resolved = candidate.resolve()
        if kb_root not in resolved.parents:
            raise FileNotFoundError(f"Note must live under {kb_root}: {resolved}")
        return resolved

    repo_candidate = (repo_root / arg).resolve()
    if repo_candidate.is_file():
        if kb_root not in repo_candidate.parents:
            raise FileNotFoundError(f"Note must live under {kb_root}: {repo_candidate}")
        return repo_candidate

    name = arg if arg.endswith(".md") else f"{arg}.md"
    matches = sorted(path.resolve() for path in kb_root.rglob(name))
    if not matches:
        matches = sorted(path.resolve() for path in kb_root.rglob("*.md") if path.stem == arg)

    if not matches:
        raise FileNotFoundError(f"No matching note found for: {arg}")
    if len(matches) > 1:
        formatted = "\n".join(str(path.relative_to(repo_root)) for path in matches)
        raise FileNotFoundError(f"Multiple matching notes found:\n{formatted}")
    return matches[0]


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


def find_repo_markdown_files(repo_root: Path) -> list[Path]:
    return sorted(
        path
        for path in repo_root.rglob("*.md")
        if not is_nested_git_repo_content(path.resolve(), repo_root)
    )


def reviews_root(kb_root: Path) -> Path:
    return kb_root / "reports" / "reviews"


def repo_relative_note_path(note_path: Path, repo_root: Path) -> str:
    return note_path.relative_to(repo_root).as_posix()


def encode_review_export_dir(note_path: str) -> str:
    stem = note_path[:-3] if note_path.endswith(".md") else note_path
    return stem.replace("/", "__")


def review_export_dir_for_note(note_path: Path, *, repo_root: Path, kb_root: Path) -> Path:
    return reviews_root(kb_root) / encode_review_export_dir(repo_relative_note_path(note_path, repo_root))


def rewrite_review_export_metadata(
    content: str,
    *,
    old_note_path: str,
    new_note_path: str,
) -> tuple[str, bool]:
    metadata = review_metadata.parse_review_metadata(content)
    if metadata is None or metadata.note_path != old_note_path:
        return content, False
    return (
        review_metadata.inject_review_metadata(
            content,
            replace(metadata, note_path=new_note_path),
        ),
        True,
    )


def collect_review_export_updates(
    source: Path,
    destination: Path,
    *,
    repo_root: Path,
    kb_root: Path,
) -> tuple[Path, Path, dict[Path, str]]:
    source_dir = review_export_dir_for_note(source, repo_root=repo_root, kb_root=kb_root)
    destination_dir = review_export_dir_for_note(destination, repo_root=repo_root, kb_root=kb_root)
    if not source_dir.is_dir():
        return source_dir, destination_dir, {}

    old_note_path = repo_relative_note_path(source, repo_root)
    new_note_path = repo_relative_note_path(destination, repo_root)
    updates: dict[Path, str] = {}
    for review_file in sorted(source_dir.rglob("*.md")):
        updated, changed = rewrite_review_export_metadata(
            review_file.read_text(encoding="utf-8"),
            old_note_path=old_note_path,
            new_note_path=new_note_path,
        )
        if changed:
            updates[review_file] = updated
    return source_dir, destination_dir, updates


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


def relocate_note(
    *,
    repo_root: Path,
    note_arg: str,
    new_name: str | None = None,
    dest_path: str | None = None,
    apply: bool = False,
) -> int:
    kb_root = repo_root / "kb"
    mkdocs_config = repo_root / "mkdocs.yml"

    source = resolve_note(note_arg, repo_root=repo_root, kb_root=kb_root)
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
    source_review_dir, destination_review_dir, review_export_updates = collect_review_export_updates(
        source,
        destination,
        repo_root=repo_root,
        kb_root=kb_root,
    )
    if source_review_dir.exists() and destination_review_dir.exists():
        print(
            (
                "Destination review export directory already exists: "
                f"{destination_review_dir.relative_to(repo_root)}"
            ),
            file=sys.stderr,
        )
        return 1

    db_path = review_db.resolve_db_path(repo_root)
    review_db_counts = None
    if db_path.exists():
        with review_db.connect(db_path) as conn:
            review_db_counts = review_db.count_note_path_records(
                conn,
                note_path=repo_relative_note_path(source, repo_root),
            )

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

    if source_review_dir.exists():
        print(
            "Review exports:"
            f" {source_review_dir.relative_to(repo_root)} -> {destination_review_dir.relative_to(repo_root)}"
        )
        if review_export_updates:
            print(f"Review export files to rewrite: {len(review_export_updates)}")
        else:
            print("Review export files to rewrite: 0")
    else:
        print("Review exports: none")

    if review_db_counts is None:
        print("Review DB updates: none")
    else:
        print(
            "Review DB updates:"
            f" review_runs={review_db_counts.review_runs},"
            f" gate_reviews={review_db_counts.gate_reviews},"
            f" acceptance_events={review_db_counts.acceptance_events}"
        )

    if not apply:
        print("\nThis was a dry run. Pass --apply to execute.")
        return 0

    strategy = move_note(source, destination, repo_root=repo_root)
    review_export_strategy = None
    if source_review_dir.exists():
        review_export_strategy = move_path(source_review_dir, destination_review_dir, repo_root=repo_root)
    for path, (updated, _changes) in markdown_updates.items():
        target = destination if path.resolve() == source else path
        target.write_text(updated, encoding="utf-8")
    for path, updated in review_export_updates.items():
        target = destination_review_dir / path.relative_to(source_review_dir)
        target.write_text(updated, encoding="utf-8")
    mkdocs_config.write_text(mkdocs_updated, encoding="utf-8")
    if review_db_counts is not None:
        with review_db.connect(db_path) as conn:
            review_db.rekey_note_path(
                conn,
                old_note_path=repo_relative_note_path(source, repo_root),
                new_note_path=repo_relative_note_path(destination, repo_root),
            )
            conn.commit()

    print(f"\nMove strategy: {strategy}")
    if review_export_strategy is not None:
        print(f"Review export move strategy: {review_export_strategy}")
    print("Done.")
    return 0
