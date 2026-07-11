"""Prompt-target preparation for review jobs."""

from __future__ import annotations

import re
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.lib.note_parser import find_markdown_links_with_text
from commonplace.review.protocol.prompt import NoteReviewTarget


URL_SCHEME_RE = re.compile(r"^[a-z]+://", re.IGNORECASE)


def resolve_note_markdown_links(
    *,
    repo_root: Path,
    note_abs: Path,
    note_body: str,
) -> tuple[list[tuple[str, str, str]], list[tuple[str, str]]]:
    resolved: list[tuple[str, str, str]] = []
    unresolved: list[tuple[str, str]] = []
    seen_resolved: set[tuple[str, str, str]] = set()
    seen_unresolved: set[tuple[str, str]] = set()

    repo_root_resolved = repo_root.resolve()
    for link_text, raw_target in find_markdown_links_with_text(note_body):
        if URL_SCHEME_RE.match(raw_target) or raw_target.startswith("#"):
            continue

        bare_target = raw_target.split("#", 1)[0]
        if not bare_target or not bare_target.endswith(".md"):
            continue

        candidate = (note_abs.parent / bare_target).resolve()
        try:
            repo_rel = candidate.relative_to(repo_root_resolved).as_posix()
        except ValueError:
            repo_rel = None

        if candidate.exists() and repo_rel is not None:
            entry = (link_text, raw_target, repo_rel)
            if entry not in seen_resolved:
                seen_resolved.add(entry)
                resolved.append(entry)
            continue

        missing = (link_text, raw_target)
        if missing not in seen_unresolved:
            seen_unresolved.add(missing)
            unresolved.append(missing)

    return resolved, unresolved


def prepare_note_target(
    *,
    repo_root: Path,
    note_path: str,
    review_job_id: int,
    criterion_paths: tuple[str, ...],
    note_text: str | None = None,
) -> NoteReviewTarget:
    note_abs = repo_root / note_path
    if note_text is None:
        note_text = note_abs.read_text(encoding="utf-8")
    note_body = frontmatter.strip(note_text).lstrip("\n")
    resolved_links, unresolved_links = resolve_note_markdown_links(
        repo_root=repo_root,
        note_abs=note_abs,
        note_body=note_body,
    )
    return NoteReviewTarget(
        note_path=note_path,
        review_job_id=review_job_id,
        criterion_paths=criterion_paths,
        note_text=note_text,
        resolved_links=resolved_links,
        unresolved_links=unresolved_links,
    )
